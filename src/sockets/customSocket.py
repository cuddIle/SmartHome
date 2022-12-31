from abc import ABC, abstractmethod


class CustomSocket(ABC):

    @abstractmethod
    def send(self, msg: str) -> None:
        pass

    @abstractmethod
    def recv(self) -> bytes:
        return
