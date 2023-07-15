from abc import ABC, abstractmethod


class AbstractResponse(ABC):

    @abstractmethod
    def success(self, **kwargs):
        return NotImplementedError('Method not implemented')

    @abstractmethod
    def error(self, **kwargs):
        return NotImplementedError('Method not implemented')