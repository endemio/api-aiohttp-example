import logging
from abc import ABC

from aiohttp.web import Response

from module.api.abstract.dto import AbstractDTOResponse
from module.api.abstract.action import AbstractAction
from module.api.abstract.response import AbstractResponse

# Parents
from module.api.endpoint.parent.rest import RestEndpoint
from module.api.endpoint.parent.jsonrpc import ResponseFormat


class RestJsonRPCMethodParent(RestEndpoint, ResponseFormat, ABC):

    def __init__(self, action: AbstractAction, transform: AbstractResponse, dto: AbstractDTOResponse):
        self.__action = action
        self.__dto = dto
        RestEndpoint.__init__(self)
        ResponseFormat.__init__(self, transform)

    def execute(self) -> Response:

        try:
            result = self.action.run()
            body = self.success(self.__dto.export(result), self.__dto.METHOD, self.action.token)
        except SystemError as err:
            body = self.error(err.__str__(), -32000, self.__dto.METHOD, self.action.token)
        except Exception:
            body = self.error('Global application error', -32100, self.__dto.METHOD, self.action.token)

        logging.debug('Body is {}'.format(body))

        # Return response
        return Response(status=200, body=body, content_type=self.CONTENT_TYPE)

    @property
    def action(self) -> AbstractAction:
        return self.__action
