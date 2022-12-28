import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from contestants import RequestsType


@dataclass
class Request(ABC):
    type: RequestsType
    src: str
    dst: str

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


@dataclass
class SigninRequest(Request):
    username: str
    password: str


class SignupRequest(Request):
    username: str
    password: str


@dataclass
class ConnectUserRequest(Request):
    user_secret: str


@dataclass
class ConnectDeviceRequest(Request):
    user_secret: str



