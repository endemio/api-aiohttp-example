import logging
from abc import ABC

from aiohttp.web import Response
from module.api.endpoint.method.parent import RestJsonRPCMethodParent


class RestJsonRPCMethodGet(RestJsonRPCMethodParent, ABC):

    def run(self, data: dict) -> Response:
        self.action.init(data)

        logging.debug('Add *args to {} response, method {}, args list {}, token {}'.format(
            self.__class__.__name__, 'GET', data, self.action.token))

        return self.execute()
