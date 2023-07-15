from abc import ABC

from module.api.abstract.dto import AbstractDTORequest


class StatusDTOApiRequest(AbstractDTORequest, ABC):

    def __new__(cls, token, *args) -> dict:
        return {'token': token}


class ServerTimeDTOApiRequest(AbstractDTORequest, ABC):

    def __new__(cls, action, token, *args) -> dict:
        return {'action': action, 'token': token}
