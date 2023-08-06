import asyncio
import warnings
from typing import (
    Any,
    List,
    Tuple,
    Union,
    Optional,
    Mapping,
    Pattern
)
from types import MethodType
from itertools import zip_longest
from multidict import CIMultiDict

import aiohttp
from yarl import URL
from aiohttp import client_exceptions as aiohttp_client_exceptions
try:
    import chardet as _chardet
except ImportError:
    import charset_normalizer as _chardet
from parsel.selector import Selector, LXML_SUPPORTS_HUGE_TREE

from pyxk.aclient.typedef import (
    StrOrURL,
    Session,
    Response,
    EventLoop,
    CIMDict,
    Timeout,
    ResponseSelector,
    RequestCallback
)
from pyxk.utils import get_user_agent



__all__ = ["chardet", "Client"]

def chardet(byte: bytes):
    """字符编码判断"""
    return _chardet.detect(byte)


class Client:
    """
    异步下载器 - 类变量

    :params: limit : 并发数量
    :params: timeout : 请求超时时间
    :params: headers : 请求头
    :params: verify_ssl : ssl验证
    :params: start_urls : 请求入口urls
    :params: user_agnet : User-Agent
    :params: aiohttp_kwargs : aiohttp.ClientSession 实例化参数
    :params: retry_status_code : 请求状态码，包含在列表中的进行重新发送
    :params: error_status_code: 请求状态码，包含在列表中直接抛出错误

    __init__ parameters - 实例化参数

    :params: loop : asyncio event loop
    :params: session : aiohttp client_session
    :params: base_url : base_url
    """
    limit: int = 16
    timeout: Timeout = 7
    headers: Optional[Union[dict, CIMDict]] = None
    verify_ssl: bool = True
    start_urls: Union[List[str], List[Tuple[str, dict]]] = []
    user_agent: str = get_user_agent("windows")
    aiohttp_kwargs: Optional[dict] = None
    retry_status_code: Optional[list] = None
    error_status_code: Optional[list] = None

    def __init__(
        self,
        *,
        loop: EventLoop=None,
        session: Session=None,
        base_url: StrOrURL=None,
    ) -> None:
        self._loop = loop
        self._session = session
        self._base_url = self.set_base_url(base_url)

    @classmethod
    def run(cls, **kwargs):
        """
        异步下载器 运行入口 - 应该从此方法运行

        :params: **kwargs : 实例化参数
        """
        if not kwargs.__contains__("loop"):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            kwargs.__setitem__("loop", loop)
        self = cls(**kwargs)
        # run
        self.loop.run_until_complete(self.async_start())
        # close event loop
        self.loop.close()
        return self

    async def async_start(self):
        """开启异步下载器"""
        # 创建 aiohttp session
        try:
            # 创建 aiohttp session
            await self.create_aiohttp_session()
            await self.start()
            result = await self.start_request()
            # 运行结束返回值 传递给 completed
            await self.completed(result)
        finally:
            await self.async_close()

    async def async_close(self):
        """关闭异步下载器"""
        await self.close()
        if self.session:
            await self.session.close()

    async def start_request(self) -> list:
        """发送 start_urls 链接"""
        # 判断 start_urls 是否为空
        if not self.start_urls:
            raise NotImplementedError(f"{self.__class__.__name__}.start_urls is empty! (must be a 'list')")
        cb_kwargs_list, start_urls = [], []
        for item in self.start_urls:
            if isinstance(item, (list, tuple)) and len(item) == 2:
                url, cb_kwargs = item
            else:
                url, cb_kwargs = item, None
            start_urls.append(url)
            cb_kwargs_list.append(cb_kwargs)
            if not self._base_url:
                self._base_url = self.set_base_url(url)
        result = await self.gather(*start_urls, callback=self.parse, cb_kwargs_list=cb_kwargs_list)
        return result

    async def request(
        self,
        url: StrOrURL,
        *,
        callback: RequestCallback=None,
        method: str="GET",
        cb_kwargs: Optional[dict]=None,
        **kwargs
    ) -> Any:
        """
        异步请求发送

        :params: url : url地址
        :params: callback : 响应response 回调函数(函数是异步的)
        :params: method : 请求方法
        :params: cb_kwargs : 回调函数 自定义参数
        :params: **kwargs : 异步请求额外参数
        """
        url = self.build_url(url)
        exc_count, exc_max = 0, 30
        response, is_close_response = None, False
        cb_kwargs = cb_kwargs if isinstance(cb_kwargs, dict) else {}
        while True:
            try:
                response = result = await self.session.request(method=method, url=url, **kwargs)
                # 错误request状态码捕获
                if (
                    isinstance(self.error_status_code, (list, tuple))
                    and response.status in self.error_status_code
                ):
                    raise aiohttp.InvalidURL(
                        f"invalid url:{str(response.url)!r}, status_code: {response.status!r}"
                    )
                # request状态码捕获 并重试
                if (
                    isinstance(self.retry_status_code, (list, tuple))
                    and response.status in self.retry_status_code
                ):
                    await asyncio.sleep(1)
                    continue
                # response 添加方法
                add_method_to_response(response)
                if callable(callback):
                    result = await callback(response, **cb_kwargs)
                    is_close_response = True
                break
            # 请求超时 重试
            except asyncio.exceptions.TimeoutError:
                exc_count += 1
                if exc_count > exc_max:
                    raise
                await asyncio.sleep(1)
            # 连接错误 重试
            except (
                aiohttp_client_exceptions.ClientOSError,
                aiohttp_client_exceptions.ClientPayloadError,
                aiohttp_client_exceptions.ClientConnectorError,
            ):
                exc_count += 1
                if exc_count > exc_max:
                    raise
                warnings.warn("Client Connector Error", stacklevel=4)
                await asyncio.sleep(1)
            # 服务器拒绝连接
            except aiohttp_client_exceptions.ServerDisconnectedError:
                exc_count += 1
                if exc_count > exc_max:
                    raise
                warnings.warn("Server Disconnected Error", stacklevel=4)
                await asyncio.sleep(1)
            finally:
                if response and is_close_response:
                    response.close()
        return result

    async def gather(
        self,
        *urls,
        callback: RequestCallback=None,
        method: str="GET",
        cb_kwargs_list: List[dict]=None,
        return_exceptions=False,
        **kwargs
    ) -> list:
        """
        收集 url列表，创建异步任务 并发发送

        :params: *urls : url 并发集合
        :params: callback : 回调函数
        :params: method : 请求方法
        :params: cb_kwargs_list : 回调函数参数列表
        :params: return_exceptions : 错误传递
        :params: **kwargs : 请求参数
        """
        # cb_kwargs_list
        if isinstance(cb_kwargs_list, dict):
            cb_kwargs_list = [cb_kwargs_list for _ in enumerate(urls)]
        elif not isinstance(cb_kwargs_list, (list, tuple)):
            cb_kwargs_list = []

        request_tasks = [
            self.request(
                url, callback=callback, method=method, cb_kwargs=cb_kwargs, **kwargs
            )
            for url, cb_kwargs in zip_longest(urls, cb_kwargs_list, fillvalue={})
        ]
        result = await asyncio.gather(
            *request_tasks,
            return_exceptions=return_exceptions
        )
        return result

    async def create_aiohttp_session(self) -> None:
        """创建 aiohttp session"""
        headers = self.merge_headers()
        aiohttp_kwargs = self.merge_aiohttp_kwargs()
        self.session = aiohttp.ClientSession(
            loop=self.loop, headers=headers, **aiohttp_kwargs
        )

    def merge_headers(self) -> CIMDict:
        """合并 headers"""
        headers = CIMultiDict(self.headers or {})
        headers.setdefault("User-Agent", self.user_agent)
        return headers

    def merge_aiohttp_kwargs(self) -> dict:
        """合并 aiohttp kwargs"""
        aiohttp_kwargs = dict(self.aiohttp_kwargs or {})
        # timeout 默认7秒
        if isinstance(self.timeout, (int, float)) and self.timeout >= 0:
            timeout = self.timeout
        elif not isinstance(self.timeout, aiohttp.ClientTimeout):
            timeout = 7
        aiohttp_kwargs.setdefault("timeout", aiohttp.ClientTimeout(total=timeout))

        # connector 默认 limit=16
        if isinstance(self.limit, int) and self.limit >= 0:
            limit = self.limit
        else:
            limit = 16
        connector = aiohttp.TCPConnector(limit=limit, loop=self.loop, verify_ssl=self.verify_ssl)
        aiohttp_kwargs.setdefault("connector", connector)
        return aiohttp_kwargs


    def build_url(self, _url) -> StrOrURL:
        """构造完整url地址"""
        if not isinstance(_url, (str, URL)):
            return _url
        _url = URL(_url)
        if _url.is_absolute():
            return _url
        if self.base_url and isinstance(self.base_url, URL):
            return self.base_url.join(_url)
        return _url

    @staticmethod
    def set_base_url(url: StrOrURL, /) -> StrOrURL:
        """设置 base_url"""
        if url is None:
            return None
        if not isinstance(url, (str, URL)):
            warnings.warn(f"{url!r} invalid base_url", stacklevel=4)
            return None
        url = URL(url)
        if not url.is_absolute():
            # 不是绝对路径
            warnings.warn(f"{url.human_repr()!r} not absolute", stacklevel=4)
            return None
        return url

    @property
    def loop(self) -> EventLoop:
        """Event Loop"""
        if not self._loop:
            self._loop = asyncio.get_event_loop()
            asyncio.set_event_loop(self._loop)
        elif isinstance(self._loop, asyncio.AbstractEventLoop):
            if self._loop.is_closed():
                warnings.warn("Current EventLoop is closed", stacklevel=4)
        return self._loop

    @loop.setter
    def loop(self, _loop: EventLoop) -> None:
        if _loop is None:
            self._loop = None
            return
        if not isinstance(_loop, asyncio.AbstractEventLoop):
            warnings.warn(f"{_loop!r} invalid EventLoop", stacklevel=4)
            self._loop = None
            return
        self._loop = _loop
        asyncio.set_event_loop(_loop)

    @property
    def base_url(self) -> StrOrURL:
        """base_url"""
        return self._base_url

    @base_url.setter
    def base_url(self, _url: StrOrURL) -> None:
        self._base_url = self.set_base_url(_url)

    @property
    def session(self) -> Session:
        """aiohttp session"""
        return self._session

    @session.setter
    def session(self, _session: Session) -> None:
        if not isinstance(_session, aiohttp.ClientSession):
            warnings.warn(f"{_session!r} invalid aiohttp session", stacklevel=4)
            return
        self._session = _session

    @staticmethod
    async def sleep(delay: Union[int, float]=0, result: Any=None) -> Any:
        """异步休眠"""
        return await asyncio.sleep(delay, result=result)

    @staticmethod
    def apparent_encoding(byte: bytes):
        return chardet(byte)["encoding"]

    async def parse(self, response: Response):
        raise NotImplementedError(f"'{self.__class__.__name__}.parse' not implemented!")

    async def completed(self, result: list) -> None:
        """运行完成结果回调函数"""

    async def start(self) -> None:
        """创建 aiohttp session 后调用"""

    async def close(self) -> None:
        """关闭 aiohttp session 前调用"""


async def xpath(
    self,
    query: str,
    namespaces: Optional[Mapping[str, str]] = None,
    encoding: Optional[str] = None,
    type: Optional[str] = None,
    root: Optional[Any] = None,
    base_url: Optional[str] = None,
    _expr: Optional[str] = None,
    huge_tree: bool = LXML_SUPPORTS_HUGE_TREE,
    errors: str = "strict",
    **kwargs
) -> ResponseSelector:
    text = await self.text(encoding=encoding, errors=errors)
    selector = Selector(
        text=text,
        type=type,
        _expr=_expr,
        namespaces=namespaces,
        root=root,
        base_url=base_url,
        huge_tree=huge_tree,
    )
    return selector.xpath(query=query, **kwargs)

async def css(
    self,
    query: str,
    namespaces: Optional[Mapping[str, str]] = None,
    encoding: Optional[str] = None,
    type: Optional[str] = None,
    root: Optional[Any] = None,
    base_url: Optional[str] = None,
    _expr: Optional[str] = None,
    huge_tree: bool = LXML_SUPPORTS_HUGE_TREE,
    errors: str = "strict"
) -> ResponseSelector:
    text = await self.text(encoding=encoding, errors=errors)
    selector = Selector(
        text=text,
        type=type,
        _expr=_expr,
        namespaces=namespaces,
        root=root,
        base_url=base_url,
        huge_tree=huge_tree,
    )
    return selector.css(query=query)

async def re(
    self,
    regex: Union[str, Pattern[str]],
    replace_entities: bool = True,
    namespaces: Optional[Mapping[str, str]] = None,
    encoding: Optional[str] = None,
    type: Optional[str] = None,
    root: Optional[Any] = None,
    base_url: Optional[str] = None,
    _expr: Optional[str] = None,
    huge_tree: bool = LXML_SUPPORTS_HUGE_TREE,
    errors: str = "strict",
) -> ResponseSelector:
    text = await self.text(encoding=encoding, errors=errors)
    selector = Selector(
        text=text,
        type=type,
        _expr=_expr,
        namespaces=namespaces,
        root=root,
        base_url=base_url,
        huge_tree=huge_tree,
    )
    return selector.re(regex=regex, replace_entities=replace_entities)

def urljoin(self, _url: Union[str, URL], /) -> StrOrURL:
    if isinstance(_url, str):
        _url = URL(_url)
    elif not isinstance(_url, URL):
        return _url
    if _url.is_absolute():
        return _url
    return self.url.join(_url)

def add_method_to_response(response: Response) -> None:
    """
    为异步response添加实例方法
    """
    response.re = MethodType(re, response)
    response.css = MethodType(css, response)
    response.xpath = MethodType(xpath, response)
    response.urljoin = MethodType(urljoin, response)
