import socket
import time
import json

import sys,os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))#存放c.py所在的绝对路径

from server_thread import ServerThread

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9001))
    server.listen(5)
    print('server run on 0.0.0.0:9001')
    client_socket_mapping = {}

    while True:
        conn, addr = server.accept()
        ServerThread(conn, client_socket_mapping).start()