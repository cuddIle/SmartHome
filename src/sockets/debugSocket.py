from src.sockets.customSocket import CustomSocket
import time


class DebugSocket(CustomSocket):
    network = dict()
    last_data_sent = bytes()

    def __init__(self, addr: tuple[str, int]):
        self.dst_addr = None
        self.addr = addr
        DebugSocket.network[str(addr)] = list()

    def connect(self, dst_addr: tuple[str, int]):
        self.dst_addr = dst_addr

    def send(self, msg):
        DebugSocket.network[str(self.dst_addr)].append(msg)

    def recv(self, timeout=30) -> bytes:
        print(DebugSocket.network)
        t = time.time() + timeout

        while t > time.time():
            if DebugSocket.network[str(self.addr)]:
                return DebugSocket.network[str(self.addr)].pop()
