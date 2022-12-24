from src.rsaSocket import RsaSocket
import pytest
import mock

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class MockSocketWrapper:
    def __int__(self, mock_socket):
        self.mock_socket = mock_socket

    def send(self, value):
        self.mock_socket.return_value.recv.return_value = value



def test_answer():
    with mock.patch('socket.socket') as mock_socket:
        test_rsa_sock = RsaSocket()
        test_rsa_sock.bind(("", 11211))
        mock_socket.return_value.send.return_value = a




