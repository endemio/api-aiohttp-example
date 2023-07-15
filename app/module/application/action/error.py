from module.application.abstract.action import AbstractAction
from module.application.dto.request import StatusDTOAppRequest


class ServerError(AbstractAction):

    def __init__(self):
        self.__token = None

    def init(self, data: dict):
        [self.__token] = StatusDTOAppRequest(data if data else {})

    def run(self) -> dict:
        # Doing something important, but fail
        # ...

        raise SystemError("This action cannot be successfully completed")

    @property
    def token(self) -> str:
        return self.__token if self.__token else ''
