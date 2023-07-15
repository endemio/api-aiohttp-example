import abc
import json

from module.api.abstract.response import AbstractResponse


class JsonRPCResponseFormat(AbstractResponse, abc.ABC):

    def success(self, **kwargs):
        return json.dumps({
            "jsonrpc": "2.0",
            "method": kwargs.get('method', None),
            "result": kwargs.get('result', {}),
            "id": kwargs.get('token', '')
        }, indent=4)

    def error(self, **kwargs):
        return json.dumps({
            "jsonrpc": "2.0",
            "method": kwargs.get('method', None),
            "error": kwargs.get('error', {}),
            "id": kwargs.get('token', '')
        }, indent=4)
