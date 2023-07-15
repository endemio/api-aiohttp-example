import os
import logging

from aiohttp_swagger import *
from aiohttp.web import Application, run_app
from aiohttp.hdrs import METH_GET

from module.api.main import API

# JsonRPC response format class
from module.api.transform.response import JsonRPCResponseFormat

# Endpoints
from module.api.endpoint.status import StatusAPI
from module.api.endpoint.time import ServerTimeAPI
from module.api.endpoint.error import ErrorAPI

# Response DTOs
from module.api.dto.response import ServerTimeDTOApiResponse
from module.api.dto.response import StatusDTOApiResponse

# Adapters
from module.adapter.time import ServerTimeAdapter
from module.adapter.status import ServerStatusAdapter
from module.adapter.error import ServerErrorAdapter

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

PATH_API_STATUS = '/api/status'
PATH_API_ERROR = '/api/error'
PATH_API_TIME = '/api/time/{action}'


async def init():
    app = Application()

    # Init API endpoints
    status = API(
        StatusAPI(ServerStatusAdapter(), JsonRPCResponseFormat(), StatusDTOApiResponse()),
        PATH_API_STATUS,
        METH_GET)
    status.register(app.router)

    time = API(
        ServerTimeAPI(ServerTimeAdapter(), JsonRPCResponseFormat(), ServerTimeDTOApiResponse()),
        PATH_API_TIME,
        METH_GET)
    time.register(app.router)

    error = API(
        ErrorAPI(ServerErrorAdapter(), JsonRPCResponseFormat(), ServerTimeDTOApiResponse()),
        PATH_API_ERROR,
        METH_GET)
    error.register(app.router)

    # Init API Doc
    setup_swagger(app,
                  swagger_url="/api/doc",
                  description="Simple example of AIOHTTP REST API",
                  title="AIOHTTP REST API example",
                  api_version="0.0.1",
                  contact="aiohttp@endemic.ru",
                  )

    return app


if __name__ == '__main__':
    run_app(init(), port=os.getenv('HTTP_PORT'))
