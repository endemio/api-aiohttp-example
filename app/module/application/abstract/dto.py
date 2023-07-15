from abc import ABC, abstractmethod


class AbstractDTORequest(ABC):

    @abstractmethod
    def __new__(cls, *args, **kwargs) -> list:
        pass


class AbstractDTOResponse(ABC):

    @abstractmethod
    def __new__(cls, *args, **kwargs):
        pass
