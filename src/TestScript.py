

from dataclasses import dataclass
from src.sockets.debugSocket import DebugSocket
from src.sockets.rsaSocket import RsaSocket

d1 = DebugSocket()
r1 = RsaSocket(d1)

r1.send("aaa")
print(r1.recv())





