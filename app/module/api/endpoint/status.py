import uuid
from aiohttp.web import Request, Response
from module.api.endpoint.method.get import RestJsonRPCMethodGet
from module.api.dto.request import StatusDTOApiRequest


class StatusAPI(RestJsonRPCMethodGet):

    async def get(self) -> Response:
        return super().run(StatusDTOApiRequest(token=uuid.uuid4().__str__()))

    def swagger(self, request: Request):
        """
        ---
        description: Endpoint yo check that REST API is working
        tags:
        - Status response
        produces:
        - application/json
        responses:
            "200":
                description: Successful operation - service is up.
            "500":
                description: Error
            "502":
                description: Service is unavailable

        """
        return self.dispatch(request)
