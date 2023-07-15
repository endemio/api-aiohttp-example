from abc import ABC, abstractmethod


class AbstractAction(ABC):
    @abstractmethod
    def init(self, data: dict):
        raise NotImplementedError("Method 'init' doesn't implement")

    @abstractmethod
    def run(self) -> dict:
        raise NotImplementedError("Method 'run' doesn't implement")

    @property
    def token(self) -> str:
        return ''
