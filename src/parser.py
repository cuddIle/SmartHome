from mypy.typeshed.stdlib.builtins import staticmethod

from requests import SigninRequest, SignupRequest, ConnectUserRequest, ConnectDeviceRequest, Request
from contestants import RequestsType
import json


class Parser:
    def __int__(self):
        pass

    @staticmethod
    def pars_request(request: str) -> Request:
        json_request = json.loads(request)
        request_type = json_request.pop("type")

        try:
            if request_type == RequestsType.SIGNIN:
                return SigninRequest(**json_request)

            elif request_type == RequestsType.SIGNUP:
                return SignupRequest(**json_request)

            elif request_type == RequestsType.CONNECT_DEVICE:
                return ConnectDeviceRequest(**json_request)

            elif request_type == RequestsType.CONNECT_USER:
                return ConnectUserRequest(**json_request)

        except TypeError:
            # TODO: make custom exception
            raise Exception(f"the request {request_type} got invalid arguments: {request}")

        else:
            # TODO: make custom exception
            raise Exception(f"invalid request type: {request_type}")


