from abc import ABC, abstractmethod
from aiohttp.web import Response, Request


class AbstractEndpoint(ABC):
    CONTENT_TYPE = None

    @abstractmethod
    def run(self, *args):
        pass

    @abstractmethod
    def success(self, **kwargs):
        raise NotImplementedError("Method 'render' doesn't implement")

    @abstractmethod
    def swagger(self, request: Request):
        raise NotImplementedError("Method 'swagger' doesn't implement")
