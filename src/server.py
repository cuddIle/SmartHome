import socket
import logging
import threading
from concurrent.futures import ThreadPoolExecutor

from clientsManager import ClientsManager
from authManager import AuthManager
from database import Database
from parser import Parser



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

    def handle_new_connection(self, new_socket: socket.socket):
        # TODO: make socket encrypted with rsa
        request_str = new_socket.recv()

        request = self.parser.pars_request(request_str)

        # TODO: pars the request
        # TODO: send the respond of the auth manager throw the encrypted socket

        pass

    def listen_for_new_connections(self):
        while True:
            client_socket, address = self.server_socket.accept()
            self.thread_pool.submit(self.handle_new_connection(), client_socket)






