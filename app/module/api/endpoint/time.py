import uuid
from aiohttp.web import Request, Response
from module.api.endpoint.method.get import RestJsonRPCMethodGet
from module.api.dto.request import ServerTimeDTOApiRequest


class ServerTimeAPI(RestJsonRPCMethodGet):

    async def get(self, action) -> Response:
        return super().run(ServerTimeDTOApiRequest(action=action, token=uuid.uuid4().__str__()))

    def swagger(self, request: Request):
        """
        ---
        description: Endpoint showing server datetime at ISO 8601 format
        tags:
        - Server response
        produces:
        - application/json
        parameters:
        - in: path
          name: action
          description: Title of action
          schema:
            type: string
            minimum: 0
          required: true
        responses:
            "200":
                description: Successful operation - service is up.
            "500":
                description: Error
            "502":
                description: Service is unavailable

        """
        return self.dispatch(request)
