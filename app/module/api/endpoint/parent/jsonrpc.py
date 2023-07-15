from abc import ABC

from module.api.abstract.endpoint import AbstractEndpoint
from module.api.abstract.response import AbstractResponse


class ResponseFormat(AbstractEndpoint, ABC):
    CONTENT_TYPE = 'application/json'

    def __init__(self, transform: AbstractResponse):
        self.__transform = transform

    def success(self, result: dict, method, token) -> str:
        return self.__transform.success(
            result=result,
            token=token,
            method=method
        )

    def error(self, error: str, code: int, method, token) -> str:
        return self.__transform.error(
            error={'code': code, 'message': error},
            token=token,
            method=method
        )
