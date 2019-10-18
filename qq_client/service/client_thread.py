import threading
import ujson as json

class ClientThread(threading.Thread):
    socket = None

    def __init__(self, socket, qq_main):
        super(ClientThread, self).__init__()
        self.socket = socket
        self.qq_main = qq_main

    def run(self):
        while True:
            data = self.socket.recv(1024)  #接收数据
            if data:
                data = json.loads(data)
                print(data)
                f = open('test.txt', 'w')
                f.write(data)