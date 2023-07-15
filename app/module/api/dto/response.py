from abc import ABC

from module.api.abstract.dto import AbstractDTOResponse
from module.api.exception import EmptyList


class StatusDTOApiResponse(AbstractDTOResponse, ABC):
    METHOD = 'info'

    def export(self, *args) -> dict:
        if not len(args):
            raise EmptyList('Empty data')
        return {'status': args[0].get('status_app', False)}


class ServerTimeDTOApiResponse(AbstractDTOResponse, ABC):
    METHOD = 'info'

    def export(self, *args) -> dict:
        if not len(args):
            raise EmptyList('Empty data')
        return {
            'datetime': args[0].get('datetime_app', ''),
            'action': args[0].get('action_app', '')
        }
