from dataclasses import dataclass


@dataclass
class Req:
    def init(self, json):
        for obj in json:
            Req[obj.key]








