import logging
import socket

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class RsaSocket:

    def __init__(self, key_size: int = 2048, public_exponent: int = 65537):

        self.client_socket = None

        # create the server private key
        self.private_key = rsa.generate_private_key(
            public_exponent=public_exponent,
            key_size=key_size,
        )

    def _start_rsa_hand_shake(self):
        logging.debug("start rsa handshake")

        # create the server public key and send it to the client
        public_key = self.private_key.public_key()
        serialized_public_key = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
        self.client_socket.send(serialized_public_key)

        # get the client public key
        pem_format_client_public_key = self.client_socket.recv()
        self.client_public_key = serialization.load_pem_private_key(pem_format_client_public_key, password=None)

    def bind(self, client_info: tuple[str, int]):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(client_info)

        self._start_rsa_hand_shake()

    def bind_socket(self, client_socket: socket.socket):
        self.client_socket = client_socket
        self._start_rsa_hand_shake()

    def send(self, msg: str):
        encrypted_msg = self.public_key.encrypt(
            msg,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        self.client_socket.send(encrypted_msg)

    def recv(self):
        encoded_msg = self.client_socket.recv()

        msg = self.private_key.decrypt(
            encoded_msg,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
