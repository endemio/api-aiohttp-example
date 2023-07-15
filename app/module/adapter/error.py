from module.application.action.error import ServerError
from module.api.abstract.action import AbstractAction


class ServerErrorAdapter(ServerError, AbstractAction):

    def __init__(self):
        super().__init__()
