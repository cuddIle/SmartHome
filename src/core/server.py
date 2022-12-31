import socket
import logging
import threading
from src.sockets.rsaSocket import RsaSocket
from src.sockets.aesSocket import AesSocket
from concurrent.futures import ThreadPoolExecutor
from src.sockets.customSocket import CustomSocket
from src.structs.contestants import RequestsType, EncryptionType
from src.structs.requests import SigninRequest, SignupRequest, ConnectUserRequest, ConnectDeviceRequest, Request
from src.core.clientsManager import ClientsManager
from src.core.authManager import AuthManager
from src.core.parser import Parser


class Server:

    SERVER_IP = ""
    SERVER_PORT = 12345
    SERVER_THREADPOOL_MAX_WORKERS = 10

    def __init__(self):
        self.clients_manager = ClientsManager()
        self.auth_manager = AuthManager()
        self.parser = Parser()

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((Server.SERVER_IP, Server.SERVER_PORT))
        self.server_socket.listen(5)

        self.thread_pool = ThreadPoolExecutor(max_workers=Server.SERVER_THREADPOOL_MAX_WORKERS)

    def run(self):
        logging.debug("running server")
        threading.Thread(target=self.listen_for_new_connections)

    def _create_encrypted_socket(self, plane_socket: socket.socket, encryption_type: EncryptionType) -> CustomSocket:
        if encryption_type == EncryptionType.AES:
            return AesSocket(plane_socket)

        elif encryption_type == EncryptionType.RSA:
            return RsaSocket(plane_socket)

    def listen_for_new_connections(self):
        while True:
            client_socket, address = self.server_socket.accept()
            self.thread_pool.submit(self.handle_new_connection(), client_socket, EncryptionType.RSA)

    def handle_new_request(self, client_socket: socket.socket, encryption_type: EncryptionType) -> None:
        # creating secure socket
        # client_socket = self._create_encrypted_socket(new_socket, encryption_type)

        request_str = client_socket.recv().decode()
        request = self.parser.pars_request(request_str)






