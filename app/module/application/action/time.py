from datetime import datetime
from module.application.abstract.action import AbstractAction

from module.application.dto.request import ServerTimeDTOAppRequest
from module.application.dto.response import ServerTimeDTOAppResponse


class ServerTime(AbstractAction):

    def __init__(self):
        self.__action = ''
        self.__token = None

    def init(self, data: dict):
        # Get data from DTO
        [self.__action, self.__token] = ServerTimeDTOAppRequest(data)

    def run(self) -> dict:
        # Doing something important
        # ...

        # Export result by DTO
        return ServerTimeDTOAppResponse(
            datetime=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            action=self.__action
        )

    @property
    def token(self) -> str:
        return self.__token if self.__token else ''
