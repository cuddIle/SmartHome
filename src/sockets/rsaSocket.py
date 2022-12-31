import logging
import socket
import sys

from src.sockets.customSocket import CustomSocket

import crypto
sys.modules['Crypto'] = crypto
from crypto.PublicKey import RSA
from crypto import Random
from crypto.Cipher import PKCS1_OAEP


class RsaSocket(CustomSocket):

    def __init__(self, client_socket, key_size: int = 2048, public_exponent: int = 65537):

        # create the server private key
        random_generator = Random.new().read
        self.private_key = RSA.generate(1024, random_generator)

        self.client_socket = client_socket
        self._start_rsa_hand_shake()

    def _start_rsa_hand_shake(self):
        logging.debug("start rsa handshake")

        # create the server public key and send it to the client
        public_key = self.private_key.public_key()
        serialized_public_key = public_key.exportKey('PEM')
        self.client_socket.send(serialized_public_key)

        # get the client public key
        pem_format_client_public_key = self.client_socket.recv()
        self.client_public_key = RSA.importKey(pem_format_client_public_key)

    def send(self, msg: str) -> None:
        cipher = PKCS1_OAEP.new(self.client_public_key)
        ciphertext = cipher.encrypt(msg.encode())
        self.client_socket.send(ciphertext)

    def recv(self) -> bytes:
        encoded_msg = self.client_socket.recv()
        cipher = PKCS1_OAEP.new(self.private_key)

        return cipher.decrypt(encoded_msg)
