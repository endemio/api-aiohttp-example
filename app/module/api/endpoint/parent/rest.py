import inspect

from aiohttp.http_exceptions import HttpBadRequest
from aiohttp.web_exceptions import HTTPMethodNotAllowed
from aiohttp.web import Request
from aiohttp.hdrs import METH_POST, METH_GET, METH_DELETE

DEFAULT_METHODS = (METH_GET, METH_POST, METH_DELETE)


class RestEndpoint:
    def __init__(self):
        self.methods = {}
        for method_name in DEFAULT_METHODS:
            method = getattr(self, method_name.lower(), None)
            if method:
                self.add_method(method_name, method)

    def add_method(self, method_name, method):
        self.methods[method_name.upper()] = method

    async def dispatch(self, request: Request):
        method = self.methods.get(request.method.upper())
        if not method:
            raise HTTPMethodNotAllowed('', DEFAULT_METHODS)

        wanted_args = list(inspect.signature(method).parameters.keys())
        available_args = request.match_info.copy()
        available_args.update({'request': request})
        unsatisfied_args = set(wanted_args) - set(available_args.keys())

        if unsatisfied_args:
            raise HttpBadRequest('There are unsatisfied_args {}'.format(unsatisfied_args))

        return await method(**{arg_name: available_args[arg_name] for arg_name in wanted_args})
