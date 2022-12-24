import socket
import ipaddress
from unittest import mock
from mock import MagicMock

from rsaSocket import RsaSocket
with mock.patch('socket.socket') as mock_socket:
    mock_socket.return_value.recv.return_value = "aaa"
    mock_socket.return_value.send.return_value = "bbb"
    soc1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc1.connect(("", 12345))
    soc1.connect.assert_called_with(("", 12345))

    print(soc1.recv())
    a = soc1.send("ccc")
    print(a)
    print("done")






