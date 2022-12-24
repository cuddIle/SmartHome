from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Request(ABC):
    type: str
    src: str
    dst: str


    pass
