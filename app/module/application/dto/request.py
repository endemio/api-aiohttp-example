from module.application.abstract.dto import AbstractDTORequest


class ServerTimeDTOAppRequest(AbstractDTORequest):

    def __new__(cls, data: dict) -> list:
        return [data.get('action', ''), data.get('token', '')]


class StatusDTOAppRequest(AbstractDTORequest):

    def __new__(cls, data: dict) -> list:
        return [data.get('token', '')]
