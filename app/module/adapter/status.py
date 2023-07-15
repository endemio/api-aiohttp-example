from module.application.action.status import ServerStatus
from module.api.abstract.action import AbstractAction


class ServerStatusAdapter(ServerStatus, AbstractAction):

    def __init__(self):
        super().__init__()
