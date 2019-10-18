from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, QGridLayout, QPushButton

from widgets.qq_input import QQInput
from widgets.qq_main_label import QQMainLabel
from widgets.qq_dialog import QQMainDialog
from service.connector import ClientService
from functools import partial
from service.client_thread import ClientThread

class QQMain(QWidget):
    user_id = ''

    def __init__(self, *args, **kwargs):
        super(QQMain, self).__init__(*args, **kwargs)
        # self.setAttribute(Qt.WA_StyledBackground, True)
        self.main_layout = QVBoxLayout(self)

        title_layout = QGridLayout(self, spacing=0)
        title_layout.setContentsMargins(0, 0, 0, 0)

        title_layout_btn1 = QQMainLabel("我的好友", self)
        title_layout_btn2 = QQMainLabel("我的消息", self)
        title_layout_btn3 = QQMainLabel("我的空间", self)
        title_layout.addWidget(title_layout_btn1, 1, 0)
        title_layout.addWidget(title_layout_btn2, 1, 1)
        title_layout.addWidget(title_layout_btn3, 1, 2)
        title_layout.setHorizontalSpacing(10)
        self.main_layout.addLayout(title_layout)

    def init_ui(self, user_id):
        self.user_id = user_id
        resp_data = ClientService().all_friends(self.user_id)

        content_layout = QVBoxLayout(self)
        for user in resp_data:
            button = QPushButton()
            button.setText(user['username'])
            content_layout.addWidget(button)
            button.clicked.connect(partial(self.show_dialog, {
                'user_id': self.user_id,
                'friend_id': user['id']
            }))


        self.main_layout.addLayout(content_layout)

        ClientThread(ClientService()._socket, self).start()

    def set_userid(self, user_id):
        self.user_id = user_id

    def show_dialog(self, user):
        self.dialog = QQMainDialog()
        self.dialog.user_id = user['user_id']
        self.dialog.friend_id = user['friend_id']
        self.dialog.user = user
        self.dialog.show()