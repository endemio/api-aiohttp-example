from abc import ABC, abstractmethod


class AbstractDTORequest(ABC):

    def __new__(cls, *args, **kwargs):
        pass


class AbstractDTOResponse(ABC):
    METHOD = 'default'

    @abstractmethod
    def export(self, *args, **kwargs) -> dict:
        pass
