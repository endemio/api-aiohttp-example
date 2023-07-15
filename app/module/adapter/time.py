from module.application.action.time import ServerTime
from module.api.abstract.action import AbstractAction


class ServerTimeAdapter(ServerTime, AbstractAction):

    def __init__(self):
        super().__init__()
