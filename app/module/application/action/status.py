from module.application.abstract.action import AbstractAction
from module.application.dto.response import StatusDTOAppResponse
from module.application.dto.request import StatusDTOAppRequest


class ServerStatus(AbstractAction):

    def __init__(self):
        self.__token = None

    def init(self, data: dict):
        [self.__token] = StatusDTOAppRequest(data if data else {})

    def run(self) -> dict:
        # Doing something important
        # ...

        # Export result by DTO
        return StatusDTOAppResponse(status=True)

    @property
    def token(self) -> str:
        return self.__token if self.__token else ''
