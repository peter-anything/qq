import ujson as json
import threading

# 建立一个服务端
from db.models.user import User
from db.tools import DBTool
from crypto import check_password
from qq_token import QQToken


class ServerThread(threading.Thread):
    def __init__(self, client_socket, client_socket_mapping):
        # 注意：一定要显式的调用父类的初始化函数。
        super(ServerThread, self).__init__()
        self.client_socket = client_socket
        self.client_socket_mapping = client_socket_mapping

    def process_login(self, conn, data):
        conn_continue = True
        db_tool = DBTool()
        params = data['parms']
        try:
            user = db_tool.get_object("select * from User where username='%s'" % params['username'], User)
        except Exception as e:
            # 登录失败，发送消息后关闭连接
            resp_data = {
                'status': 1,
                'msg': 'username or password error'
            }
            print('login error')
            conn.send(json.dumps(resp_data).encode('utf-8'))
            return False

        if check_password(params['password'], user.password):
            self.client_socket_mapping[str(user.id)] = conn
            resp_data = {
                'status': 0,
                'data': {
                    'token': QQToken.encode(user.id),
                    'id': str(user.id)
                },
                'msg': 'success'
            }
            print('login success')
            conn.send(json.dumps(resp_data).encode('utf-8'))
        else:
            # 登录失败，发送消息后关闭连接
            resp_data = {
                'status': 1,
                'msg': 'username or password error'
            }
            print('login error')
            conn.send(json.dumps(resp_data).encode('utf-8'))
            conn_continue = False

        return conn_continue

    def handle_msg(self, conn, msg):
        data = json.loads(msg)
        if data['type'] == 'USER_LOGIN':
            return self.process_login(conn, data)

        if data['type'] == 'GET_ALL_MY_FRIENDS':
            db_tool = DBTool()
            params = data['parms']
            token = params['token']
            users = db_tool.get_objects('select * from User', User)
            resp_users = []
            for user in users:
                resp_users.append(user.serialized_obj)
            conn.send(json.dumps(resp_users).encode('utf-8'))

            return True

        if data['type'] == 'SEND_MSG_TO_FRIEND':
            params = data['parms']
            user_id = params['user_id']
            msg = params['msg']

            to_friend_data = {
                user_id: 2,
                msg: 'I got it!'
            }
            friend_conn = self.client_socket_mapping[str(user_id)]
            print(self.client_socket_mapping)
            print(friend_conn)
            if friend_conn:
                friend_conn.send(json.dumps(to_friend_data).encode('utf-8'))

                resp_data = {
                    'status': 0,
                    'msg': 'send msg to friend success'
                }
                conn.send(json.dumps(resp_data).encode('utf-8'))

            return True

    def run(self):
        data = self.client_socket.recv(1024)  # 接收数据

        while True:
            if data and self.handle_msg(self.client_socket, data):
                data = self.client_socket.recv(1024)  # 接收数据
            else:
                self.client_socket.close()
                break
