from src.sockets.customSocket import CustomSocket


class DebugSocket(CustomSocket):

    last_data_sent = bytes()

    def send(self, msg):
        DebugSocket.last_data_sent = msg

    def recv(self) -> bytes:
        return DebugSocket.last_data_sent

