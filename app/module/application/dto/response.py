from module.application.abstract.dto import AbstractDTOResponse


class StatusDTOAppResponse(AbstractDTOResponse):

    def __new__(cls, **kwargs):
        return {'status_app': kwargs.get('status', False) if kwargs.get('status', False) else False}


class ServerTimeDTOAppResponse(AbstractDTOResponse):

    def __new__(cls, **kwargs):
        return {
            'datetime_app': kwargs.get('datetime', None) if kwargs.get('datetime', None) else '',
            'action_app': kwargs.get('action', None) if kwargs.get('action', None) else ''
        }
