"""ONVIF Client."""
import asyncio
import contextlib
import datetime as dt
from functools import lru_cache
import logging
import os.path
import ssl
from typing import Any, Awaitable, Callable, Dict, Optional, ParamSpec, Tuple, TypeVar

import httpx
from httpx import AsyncClient, BasicAuth, DigestAuth, TransportError
from zeep.cache import SqliteCache
from zeep.client import AsyncClient as BaseZeepAsyncClient, Settings
from zeep.exceptions import Fault, XMLSyntaxError
import zeep.helpers
from zeep.loader import parse_xml
from zeep.proxy import AsyncServiceProxy
from zeep.transports import AsyncTransport, Transport
from zeep.wsa import WsAddressingPlugin
from zeep.wsdl import Document
from zeep.wsdl.bindings.soap import SoapOperation
from zeep.wsse.username import UsernameToken

from onvif.definition import SERVICES
from onvif.exceptions import ONVIFAuthError, ONVIFError, ONVIFTimeoutError

logger = logging.getLogger("onvif")
logging.basicConfig(level=logging.INFO)
logging.getLogger("zeep.client").setLevel(logging.CRITICAL)

_DEFAULT_SETTINGS = Settings()
_DEFAULT_SETTINGS.strict = False
_DEFAULT_SETTINGS.xml_huge_tree = True

_WSDL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "wsdl")

_DEFAULT_TIMEOUT = 90
_PULLPOINT_TIMEOUT = 90
_CONNECT_TIMEOUT = 30
_READ_TIMEOUT = 90
_WRITE_TIMEOUT = 90


KEEPALIVE_EXPIRY = 4
BACKOFF_TIME = KEEPALIVE_EXPIRY + 0.5
HTTPX_LIMITS = httpx.Limits(keepalive_expiry=4)


DEFAULT_ATTEMPTS = 2

P = ParamSpec("P")
T = TypeVar("T")


def retry_connection_error(
    attempts: int = DEFAULT_ATTEMPTS,
) -> Callable[[Callable[P, Awaitable[T]]], Callable[P, Awaitable[T]]]:
    """Define a wrapper to retry on connection error."""

    def _decorator_retry_connection_error(
        func: Callable[P, Awaitable[T]]
    ) -> Callable[P, Awaitable[T]]:
        """Define a wrapper to retry on connection error.

        The remote server is allowed to disconnect us any time so
        we need to retry the operation.
        """

        async def _async_wrap_connection_error_retry(  # type: ignore[return]
            *args: P.args, **kwargs: P.kwargs
        ) -> T:
            for attempt in range(attempts):
                try:
                    return await func(*args, **kwargs)
                except httpx.RequestError as ex:
                    #
                    # We should only need to retry on RemoteProtocolError but some cameras
                    # are flakey and sometimes do not respond to the Renew request so we
                    # retry on RequestError as well.
                    #
                    # For RemoteProtocolError:
                    # http://datatracker.ietf.org/doc/html/rfc2616#section-8.1.4 allows the server
                    # to close the connection at any time, we treat this as a normal and try again
                    # once since we do not want to declare the camera as not supporting PullPoint
                    # if it just happened to close the connection at the wrong time.
                    if attempt == attempts - 1:
                        raise
                    logger.debug(
                        "Error: %s while calling %s, backing off: %s, retrying...",
                        ex,
                        func,
                        BACKOFF_TIME,
                        exc_info=True,
                    )
                    await asyncio.sleep(BACKOFF_TIME)

        return _async_wrap_connection_error_retry

    return _decorator_retry_connection_error


def create_no_verify_ssl_context() -> ssl.SSLContext:
    """Return an SSL context that does not verify the server certificate.
    This is a copy of aiohttp's create_default_context() function, with the
    ssl verify turned off and old SSL versions enabled.

    https://github.com/aio-libs/aiohttp/blob/33953f110e97eecc707e1402daa8d543f38a189b/aiohttp/connector.py#L911
    """
    sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    sslcontext.check_hostname = False
    sslcontext.verify_mode = ssl.CERT_NONE
    # Allow all ciphers rather than only Python 3.10 default
    sslcontext.set_ciphers("DEFAULT")
    with contextlib.suppress(AttributeError):
        # This only works for OpenSSL >= 1.0.0
        sslcontext.options |= ssl.OP_NO_COMPRESSION
    sslcontext.set_default_verify_paths()
    return sslcontext


_NO_VERIFY_SSL_CONTEXT = create_no_verify_ssl_context()


def safe_func(func):
    """Ensure methods to raise an ONVIFError Exception when some thing was wrong."""

    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            raise ONVIFError(err)

    return wrapped


class UsernameDigestTokenDtDiff(UsernameToken):
    """
    UsernameDigestToken class, with a time offset parameter that can be adjusted;
    This allows authentication on cameras without being time synchronized.
    Please note that using NTP on both end is the recommended solution,
    this should only be used in "safe" environments.
    """

    def __init__(self, user, passw, dt_diff=None, **kwargs):
        super().__init__(user, passw, **kwargs)
        # Date/time difference in datetime.timedelta
        self.dt_diff = dt_diff

    def apply(self, envelope, headers):
        old_created = self.created
        if self.created is None:
            self.created = dt.datetime.utcnow()
        if self.dt_diff is not None:
            self.created += self.dt_diff
        result = super().apply(envelope, headers)
        self.created = old_created
        return result


class AsyncSafeTransport(Transport):
    """A transport that blocks all remote I/O for zeep."""

    def load(self, url: str) -> None:
        """Load the given XML document."""
        if not _path_isfile(url):
            raise RuntimeError(f"Loading {url} is not supported in async mode")
        # Ideally this would happen in the executor but the library
        # does not call this from a coroutine so the best we can do
        # without a major refactor is to cache this so it only happens
        # once per process at startup. Previously it would happen once
        # per service per camera per setup which is a lot of blocking
        # I/O in the event loop so this is a major improvement.
        with open(os.path.expanduser(url), "rb") as fh:
            return fh.read()


_ASYNC_TRANSPORT = AsyncSafeTransport()


@lru_cache(maxsize=128)
def _cached_document(url: str) -> Document:
    """Load external XML document from disk."""
    return Document(url, _ASYNC_TRANSPORT, settings=_DEFAULT_SETTINGS)


class ZeepAsyncClient(BaseZeepAsyncClient):
    """Overwrite create_service method to be async."""

    def create_service(self, binding_name, address):
        """Create a new ServiceProxy for the given binding name and address.
        :param binding_name: The QName of the binding
        :param address: The address of the endpoint
        """
        try:
            binding = self.wsdl.bindings[binding_name]
        except KeyError:
            raise ValueError(
                "No binding found with the given QName. Available bindings "
                "are: %s" % (", ".join(self.wsdl.bindings.keys()))
            )
        return AsyncServiceProxy(self, binding, address=address)


# This does blocking I/O (stat) so we cache the result
# to minimize the impact of the blocking I/O.
_path_isfile = lru_cache(maxsize=128)(os.path.isfile)


class ONVIFService:
    """
    Python Implemention for ONVIF Service.
    Services List:
        DeviceMgmt DeviceIO Event AnalyticsDevice Display Imaging Media
        PTZ Receiver RemoteDiscovery Recording Replay Search Extension

    >>> from onvif import ONVIFService
    >>> device_service = ONVIFService('http://192.168.0.112/onvif/device_service',
    ...                           'admin', 'foscam',
    ...                           '/etc/onvif/wsdl/devicemgmt.wsdl')
    >>> ret = device_service.GetHostname()
    >>> print ret.FromDHCP
    >>> print ret.Name
    >>> device_service.SetHostname(dict(Name='newhostname'))
    >>> ret = device_service.GetSystemDateAndTime()
    >>> print ret.DaylightSavings
    >>> print ret.TimeZone
    >>> dict_ret = device_service.to_dict(ret)
    >>> print dict_ret['TimeZone']

    There are two ways to pass parameter to services methods
    1. Dict
        params = {'Name': 'NewHostName'}
        device_service.SetHostname(params)
    2. Type Instance
        params = device_service.create_type('SetHostname')
        params.Hostname = 'NewHostName'
        device_service.SetHostname(params)
    """

    @safe_func
    def __init__(
        self,
        xaddr: str,
        user: Optional[str],
        passwd: Optional[str],
        url: str,
        encrypt=True,
        no_cache=False,
        dt_diff=None,
        binding_name="",
        binding_key="",
        read_timeout: Optional[int] = None,
        write_timeout: Optional[int] = None,
        enable_wsa: bool = False,
    ) -> None:
        if not _path_isfile(url):
            raise ONVIFError("%s doesn`t exist!" % url)

        self.url = url
        self.xaddr = xaddr
        self.binding_key = binding_key
        # Set soap header for authentication
        self.user = user
        self.passwd = passwd
        # Indicate wether password digest is needed
        self.encrypt = encrypt
        self.dt_diff = dt_diff
        self.binding_name = binding_name
        # Create soap client
        timeouts = httpx.Timeout(
            _DEFAULT_TIMEOUT,
            connect=_CONNECT_TIMEOUT,
            read=read_timeout or _READ_TIMEOUT,
            write=write_timeout or _WRITE_TIMEOUT,
        )
        client = AsyncClient(
            verify=_NO_VERIFY_SSL_CONTEXT, timeout=timeouts, limits=HTTPX_LIMITS
        )
        # The wsdl client should never actually be used, but it is required
        # to avoid creating another ssl context since the underlying code
        # will try to create a new one if it doesn't exist.
        wsdl_client = httpx.Client(
            verify=_NO_VERIFY_SSL_CONTEXT, timeout=timeouts, limits=HTTPX_LIMITS
        )
        self.transport = (
            AsyncTransport(client=client, wsdl_client=wsdl_client)
            if no_cache
            else AsyncTransport(
                client=client, wsdl_client=wsdl_client, cache=SqliteCache()
            )
        )
        self.document: Optional[Document] = None
        self.zeep_client_authless: Optional[ZeepAsyncClient] = None
        self.ws_client_authless: Optional[AsyncServiceProxy] = None
        self.zeep_client: Optional[ZeepAsyncClient] = None
        self.ws_client: Optional[AsyncServiceProxy] = None
        self.create_type: Optional[Callable] = None
        self.loop = asyncio.get_event_loop()
        self._enable_wsa = enable_wsa

    async def setup(self):
        """Setup the transport."""
        settings = _DEFAULT_SETTINGS
        binding_name = self.binding_name
        wsse = UsernameDigestTokenDtDiff(
            self.user, self.passwd, dt_diff=self.dt_diff, use_digest=self.encrypt
        )
        self.document = await self.loop.run_in_executor(
            None, _cached_document, self.url
        )
        # Some cameras never return a response to GetCapabilities if WS-Addressing is enabled
        # but some cameras require WS-Addressing to be enabled for PullPoint or events to work
        # so we have a flag to enable/disable it which can be changed per service.
        plugins = [WsAddressingPlugin()] if self._enable_wsa else []
        self.zeep_client_authless = ZeepAsyncClient(
            wsdl=self.document,
            transport=self.transport,
            settings=settings,
            plugins=plugins,
        )
        self.ws_client_authless = self.zeep_client_authless.create_service(
            binding_name, self.xaddr
        )
        self.zeep_client = ZeepAsyncClient(
            wsdl=self.document,
            wsse=wsse,
            transport=self.transport,
            settings=settings,
            plugins=plugins,
        )
        self.ws_client = self.zeep_client.create_service(binding_name, self.xaddr)
        namespace = binding_name[binding_name.find("{") + 1 : binding_name.find("}")]
        available_ns = self.zeep_client.namespaces
        active_ns = (
            list(available_ns.keys())[list(available_ns.values()).index(namespace)]
            or "ns0"
        )
        self.create_type = lambda x: self.zeep_client.get_element(active_ns + ":" + x)()

    async def close(self):
        """Close the transport."""
        await self.transport.aclose()

    @staticmethod
    @safe_func
    def to_dict(zeepobject):
        """Convert a WSDL Type instance into a dictionary."""
        return {} if zeepobject is None else zeep.helpers.serialize_object(zeepobject)

    def __getattr__(self, name):
        """
        Call the real onvif Service operations,
        See the official wsdl definition for the
        APIs detail(API name, request parameters,
        response parameters, parameter types, etc...)
        """

        def service_wrapper(func):
            """Wrap service call."""

            @safe_func
            def wrapped(params=None):
                def call(params=None):
                    # No params
                    if params is None:
                        params = {}
                    else:
                        params = ONVIFService.to_dict(params)
                    try:
                        ret = func(**params)
                    except TypeError:
                        ret = func(params)
                    return ret

                return call(params)

            return wrapped

        builtin = name.startswith("__") and name.endswith("__")
        if builtin:
            return self.__dict__[name]
        if name.startswith("authless_"):
            return service_wrapper(getattr(self.ws_client_authless, name.split("_")[1]))
        return service_wrapper(getattr(self.ws_client, name))


class NotificationManager:
    """Manager to process notifications."""

    def __init__(self, device: "ONVIFCamera", config: Dict[str, Any]) -> None:
        """Initialize the notification processor."""
        self._service: Optional[ONVIFService] = None
        self._operation: Optional[SoapOperation] = None
        self._device = device
        self._config = config

    async def setup(self) -> ONVIFService:
        """Setup the notification processor."""
        notify_service = await self._device.create_notification_service()
        notify_subscribe = await notify_service.Subscribe(self._config)
        # pylint: disable=protected-access
        self._device.xaddrs[
            "http://www.onvif.org/ver10/events/wsdl/NotificationConsumer"
        ] = notify_subscribe.SubscriptionReference.Address._value_1
        # Create subscription manager
        # 5.2.3 BASIC NOTIFICATION INTERFACE - NOTIFY
        # Call SetSynchronizationPoint to generate a notification message
        # to ensure the webhooks are working.
        #
        # If this fails this is OK as it just means we will switch
        # to webhook later when the first notification is received.
        # WSAs enabled per
        # https://github.com/home-assistant/core/issues/83524 https://github.com/home-assistant/core/issues/45513
        service = await self._device.create_onvif_service(
            "pullpoint", port_type="NotificationConsumer", enable_wsa=True
        )
        self._operation = service.document.bindings[service.binding_name].get(
            "PullMessages"
        )
        self._service = service
        return await self._device.create_subscription_service("NotificationConsumer")

    async def start(self) -> None:
        """Start the notification processor."""
        assert self._service, "Call setup first"
        try:
            await self._service.SetSynchronizationPoint()
        except (Fault, asyncio.TimeoutError, TransportError, TypeError):
            logger.debug("%s: SetSynchronizationPoint failed", self._service.url)

    def process(self, content: bytes) -> Optional[Any]:
        """Process a notification message."""
        if not self._operation:
            logger.debug("%s: Notifications not setup", self._device.host)
            return
        try:
            envelope = parse_xml(
                content,  # type: ignore[arg-type]
                _ASYNC_TRANSPORT,
                settings=_DEFAULT_SETTINGS,
            )
        except XMLSyntaxError as exc:
            logger.error("Received invalid XML: %s", exc)
            return None
        return self._operation.process_reply(envelope)


class ONVIFCamera:
    """
    Python Implementation ONVIF compliant device
    This class integrates onvif services

    adjust_time parameter allows authentication on cameras without being time synchronized.
    Please note that using NTP on both end is the recommended solution,
    this should only be used in "safe" environments.
    Also, this cannot be used on AXIS camera, as every request is authenticated, contrary to ONVIF standard

    >>> from onvif import ONVIFCamera
    >>> mycam = ONVIFCamera('192.168.0.112', 80, 'admin', '12345')
    >>> mycam.devicemgmt.GetServices(False)
    >>> media_service = mycam.create_media_service()
    >>> ptz_service = mycam.create_ptz_service()
    # Get PTZ Configuration:
    >>> mycam.ptz.GetConfiguration()
    # Another way:
    >>> ptz_service.GetConfiguration()
    """

    def __init__(
        self,
        host: str,
        port: int,
        user: Optional[str],
        passwd: Optional[str],
        wsdl_dir: str = _WSDL_PATH,
        encrypt=True,
        no_cache=False,
        adjust_time=False,
    ) -> None:
        os.environ.pop("http_proxy", None)
        os.environ.pop("https_proxy", None)
        self.host = host
        self.port = int(port)
        self.user = user
        self.passwd = passwd
        self.wsdl_dir = wsdl_dir
        self.encrypt = encrypt
        self.no_cache = no_cache
        self.adjust_time = adjust_time
        self.dt_diff = None
        self.xaddrs = {}
        self._capabilities: Optional[Dict[str, Any]] = None

        # Active service client container
        self.services: Dict[Tuple[str, Optional[str]], ONVIFService] = {}

        self.to_dict = ONVIFService.to_dict

        self._snapshot_uris = {}
        self._snapshot_client = AsyncClient(verify=_NO_VERIFY_SSL_CONTEXT)

    async def get_capabilities(self) -> Dict[str, Any]:
        """Get device capabilities."""
        if self._capabilities is None:
            await self.update_xaddrs()
        return self._capabilities

    async def update_xaddrs(self):
        """Update xaddrs for services."""
        self.dt_diff = None
        devicemgmt = await self.create_devicemgmt_service()
        if self.adjust_time:
            try:
                sys_date = await devicemgmt.authless_GetSystemDateAndTime()
            except zeep.exceptions.Fault:
                # Looks like we should try with auth
                sys_date = await devicemgmt.GetSystemDateAndTime()
            cdate = sys_date.UTCDateTime
            cam_date = dt.datetime(
                cdate.Date.Year,
                cdate.Date.Month,
                cdate.Date.Day,
                cdate.Time.Hour,
                cdate.Time.Minute,
                cdate.Time.Second,
            )
            self.dt_diff = cam_date - dt.datetime.utcnow()
            await devicemgmt.close()
            del self.services[devicemgmt.binding_key]
            devicemgmt = await self.create_devicemgmt_service()

        # Get XAddr of services on the device
        self.xaddrs = {}
        capabilities = await devicemgmt.GetCapabilities({"Category": "All"})
        for name in capabilities:
            capability = capabilities[name]
            try:
                if name.lower() in SERVICES and capability is not None:
                    namespace = SERVICES[name.lower()]["ns"]
                    self.xaddrs[namespace] = capability["XAddr"]
            except Exception:
                logger.exception("Unexpected service type")
        try:
            self._capabilities = self.to_dict(capabilities)
        except Exception:
            logger.exception("Failed to parse capabilities")

    async def create_pullpoint_subscription(
        self, config: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Create a pullpoint subscription."""
        try:
            events = await self.create_events_service()
            pullpoint = await events.CreatePullPointSubscription(config or {})
            # pylint: disable=protected-access
            self.xaddrs[
                "http://www.onvif.org/ver10/events/wsdl/PullPointSubscription"
            ] = pullpoint.SubscriptionReference.Address._value_1
        except Fault:
            return False
        return True

    def create_notification_manager(
        self, config: Optional[Dict[str, Any]] = None
    ) -> NotificationManager:
        """Create a notification manager."""
        return NotificationManager(self, config)

    async def close(self) -> None:
        """Close all transports."""
        await self._snapshot_client.aclose()
        for service in self.services.values():
            await service.close()

    async def get_snapshot_uri(self, profile_token: str) -> str:
        """Get the snapshot uri for a given profile."""
        uri = self._snapshot_uris.get(profile_token)
        if uri is None:
            media_service = await self.create_media_service()
            req = media_service.create_type("GetSnapshotUri")
            req.ProfileToken = profile_token
            result = await media_service.GetSnapshotUri(req)
            uri = result.Uri
            self._snapshot_uris[profile_token] = uri
        return uri

    async def get_snapshot(
        self, profile_token: str, basic_auth: bool = False
    ) -> Optional[bytes]:
        """Get a snapshot image from the camera."""
        uri = await self.get_snapshot_uri(profile_token)
        if uri is None:
            return None

        auth = None
        if self.user and self.passwd:
            if basic_auth:
                auth = BasicAuth(self.user, self.passwd)
            else:
                auth = DigestAuth(self.user, self.passwd)

        try:
            response = await self._snapshot_client.get(uri, auth=auth)
        except httpx.TimeoutException as error:
            raise ONVIFTimeoutError(error) from error
        except httpx.RequestError as error:
            raise ONVIFError(error) from error

        if response.status_code == 401:
            raise ONVIFAuthError(f"Failed to authenticate to {uri}")

        if response.status_code < 300:
            return response.content

        return None

    def get_definition(
        self, name: str, port_type: Optional[str] = None
    ) -> Tuple[str, str, str]:
        """Returns xaddr and wsdl of specified service"""
        # Check if the service is supported
        if name not in SERVICES:
            raise ONVIFError("Unknown service %s" % name)
        wsdl_file = SERVICES[name]["wsdl"]
        namespace = SERVICES[name]["ns"]

        binding_name = "{{{}}}{}".format(namespace, SERVICES[name]["binding"])

        if port_type:
            namespace += "/" + port_type

        wsdlpath = os.path.join(self.wsdl_dir, wsdl_file)
        if not _path_isfile(wsdlpath):
            raise ONVIFError("No such file: %s" % wsdlpath)

        # XAddr for devicemgmt is fixed:
        if name == "devicemgmt":
            xaddr = "{}:{}/onvif/device_service".format(
                self.host
                if (self.host.startswith("http://") or self.host.startswith("https://"))
                else "http://%s" % self.host,
                self.port,
            )
            return xaddr, wsdlpath, binding_name

        # Get other XAddr
        xaddr = self.xaddrs.get(namespace)
        if not xaddr:
            raise ONVIFError("Device doesn`t support service: %s" % name)

        return xaddr, wsdlpath, binding_name

    async def create_onvif_service(
        self,
        name: str,
        port_type: Optional[str] = None,
        read_timeout: Optional[int] = None,
        write_timeout: Optional[int] = None,
        enable_wsa: bool = False,
    ) -> ONVIFService:
        """Create ONVIF service client"""
        name = name.lower()
        # Don't re-create bindings if the xaddr remains the same.
        # The xaddr can change when a new PullPointSubscription is created.
        binding_key = (name, port_type)

        xaddr, wsdl_file, binding_name = self.get_definition(name, port_type)

        existing_service = self.services.get(binding_key)
        if existing_service:
            if existing_service.xaddr == xaddr:
                return existing_service
            else:
                # Close the existing service since it's no longer valid.
                # This can happen when a new PullPointSubscription is created.
                logger.debug(
                    "Closing service %s with %s", binding_key, existing_service.xaddr
                )
                # Hold a reference to the task so it doesn't get
                # garbage collected before it completes.
                await existing_service.close()
            self.services.pop(binding_key)

        logger.debug("Creating service %s with %s", binding_key, xaddr)

        service = ONVIFService(
            xaddr,
            self.user,
            self.passwd,
            wsdl_file,
            self.encrypt,
            no_cache=self.no_cache,
            dt_diff=self.dt_diff,
            binding_name=binding_name,
            binding_key=binding_key,
            read_timeout=read_timeout,
            write_timeout=write_timeout,
            enable_wsa=enable_wsa,
        )
        await service.setup()

        self.services[binding_key] = service

        return service

    async def create_devicemgmt_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("devicemgmt")

    async def create_media_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("media")

    async def create_ptz_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("ptz")

    async def create_imaging_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("imaging")

    async def create_deviceio_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("deviceio")

    async def create_events_service(self) -> ONVIFService:
        """Service creation helper.

        WSAs enabled per
        https://github.com/home-assistant/core/issues/83524 https://github.com/home-assistant/core/issues/45513
        """
        return await self.create_onvif_service("events", enable_wsa=True)

    async def create_analytics_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("analytics")

    async def create_recording_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("recording")

    async def create_search_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("search")

    async def create_replay_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("replay")

    async def create_pullpoint_service(self) -> ONVIFService:
        """Service creation helper.

        WSAs enabled per
        https://github.com/home-assistant/core/issues/83524 https://github.com/home-assistant/core/issues/45513
        """
        return await self.create_onvif_service(
            "pullpoint",
            port_type="PullPointSubscription",
            read_timeout=_PULLPOINT_TIMEOUT,
            write_timeout=_PULLPOINT_TIMEOUT,
            enable_wsa=True,
        )

    async def create_notification_service(self) -> ONVIFService:
        """Service creation helper.

        WSAs enabled per
        https://github.com/home-assistant/core/issues/83524 https://github.com/home-assistant/core/issues/45513
        """
        return await self.create_onvif_service("notification", enable_wsa=True)

    async def create_subscription_service(
        self, port_type: Optional[str] = None
    ) -> ONVIFService:
        """Service creation helper.

        WSAs enabled per
        https://github.com/home-assistant/core/issues/83524 https://github.com/home-assistant/core/issues/45513
        """
        return await self.create_onvif_service(
            "subscription", port_type=port_type, enable_wsa=True
        )

    async def create_receiver_service(self) -> ONVIFService:
        """Service creation helper."""
        return await self.create_onvif_service("receiver")
