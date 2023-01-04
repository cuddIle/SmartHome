import threading
from dataclasses import dataclass
from src.sockets.debugSocket import DebugSocket
from src.sockets.rsaSocket import RsaSocket


def func1():
    d = DebugSocket(("1.1.1.1", 10))
    d.connect(("2.2.2.2", 10))
    r = RsaSocket(d)
    r.send("aaaa")
    print("1.1.1.1 got:", r.recv())


def func2():
    d = DebugSocket(("2.2.2.2", 10))

    d.connect(("1.1.1.1", 10))
    r = RsaSocket(d)
    print("2.2.2.2 got:", r.recv())
    r.send("aaaa")

threading.Thread(target=func2).start()
threading.Thread(target=func1).start()




