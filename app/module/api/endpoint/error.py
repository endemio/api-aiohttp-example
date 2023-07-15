import uuid
from aiohttp.web import Request, Response
from module.api.endpoint.method.get import RestJsonRPCMethodGet
from module.api.dto.request import StatusDTOApiRequest


class ErrorAPI(RestJsonRPCMethodGet):

    async def get(self) -> Response:
        return super().run(StatusDTOApiRequest(token=uuid.uuid4().__str__()))

    def swagger(self, request: Request):
        """
        ---
        description: Endpoint raise error during send request to this endpoint
        tags:
        - Status response
        produces:
        - application/json
        responses:
            "200":
                description: Successful operation.
            "500":
                description: Error
            "502":
                description: Service is unavailable

        """
        return self.dispatch(request)
