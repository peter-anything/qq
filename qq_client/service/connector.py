import socket  # 导入 socket 模块
import ujson as json


class SingleTon(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingleTon, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class ClientService(object, metaclass=SingleTon):
    _server_host = '192.168.1.143' #
    _server_port = 9001  # 设置端口号
    _socket = None

    USER_LOGIN_REQUEST = {
        'type': 'USER_LOGIN',
        'parms': {
            'username': 'peter2',
            'password': '123456'
        }
    }

    GET_ALL_MY_FRIENDS_REQUEST = {
        'type': 'GET_ALL_MY_FRIENDS',
        'parms': {
            'token': ''
        }
    }

    SEND_MSG_TO_FRIEND_REQUEST = {
        'type': 'SEND_MSG_TO_FRIEND',
        'parms': {
            'msg': 'hello, world!',
            'user_id': 1
        }
    }

    @property
    def socket(self):
        if self._socket:
            return self._socket

        self._socket = socket.socket()
        self._socket.connect((self._server_host, self._server_port))
        return self._socket

    def send_msg(self, msg):
        self.socket.send(json.dumps(msg).encode('utf-8'))
        data = self._socket.recv(1024)
        while True:
            if data:
                resp_data = json.loads(data.decode('utf-8'))
                break

        return resp_data

    def login(self, username, password):
        login_req_data = self.USER_LOGIN_REQUEST
        login_req_data['parms']['username'] = username
        login_req_data['parms']['password'] = password

        login_resp = self.send_msg(login_req_data)

        return login_resp

    def all_friends(self, username):
        all_friends_req = self.GET_ALL_MY_FRIENDS_REQUEST

        all_friends_resp = self.send_msg(all_friends_req)

        return all_friends_resp

    def send_msg_to_friend(self, user_id, friend_id, msg):
        send_msg_req = self.SEND_MSG_TO_FRIEND_REQUEST
        send_msg_req['parms']['user_id'] = friend_id

        send_msg_resp = self.send_msg(send_msg_req)

        return send_msg_req

    def wait_data_from_server(self):
        data = self.socket.recv(1024)  #接收数据
        if data:
            data = json.loads(data)
            print(data)

print(id(ClientService()))