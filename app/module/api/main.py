from aiohttp.web_urldispatcher import UrlDispatcher
from module.api.endpoint.parent.jsonrpc import ResponseFormat


class API:
    def __init__(self, endpoint: ResponseFormat, route: str, method: str):
        self.__app = endpoint
        self.__route = route
        self.__method = method

    def register(self, router: UrlDispatcher):
        router.add_route(self.__method, self.__route, self.__app.swagger)
