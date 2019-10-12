import socket  # 导入 socket 模块
import ujson as json
import time

server_host = '192.168.1.138' #
server_port = 9001  # 设置端口号

USER_LOGIN_REQUEST = {
    'type': 'USER_LOGIN',
    'parms': {
        'username': 'peter',
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
        'user_id': 2
    }
}

client_socket = socket.socket()  # 创建 socket 对象
client_socket.connect((server_host, server_port))

def send_msg(client_socket, msg):
    client_socket.send(json.dumps(msg).encode('utf-8'))
    data = client_socket.recv(1024)
    if data:
        resp_data = json.loads(data.decode('utf-8'))

    return resp_data

login_resp_data = send_msg(client_socket, USER_LOGIN_REQUEST)

if login_resp_data['status'] == 0:
    token = login_resp_data['data']['token']

    all_my_friends_req = GET_ALL_MY_FRIENDS_REQUEST
    all_my_friends_req['parms']['token'] = token

    all_my_friends_resp = send_msg(client_socket, all_my_friends_req)
    print(all_my_friends_resp)

while True:
    data = client_socket.recv(1024)  #接收数据
    if data:
        data = json.loads(data)
        print(data)

