from PyQt5.QtCore import pyqtSignal, Qt, QSize
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QTextEdit, QLineEdit

from widgets.qq_input import QQInput
from PyQt5.QtCore import pyqtSlot
from service.connector import ClientService


class QQMainDialog(QWidget):
    loginSuccess = pyqtSignal()
    user_id = ''
    friend_id = ''

    def __init__(self, *args, **kwargs):
        super(QQMainDialog, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        main_layout = QVBoxLayout()
        self.showEdit = QTextEdit()
        self.sendEdit = QTextEdit()
        self.sendButton = QPushButton()
        self.sendButton.setText('发送')
        self.sendButton.clicked.connect(self.send_msg)
        main_layout.addWidget(self.showEdit)
        main_layout.addWidget(self.sendEdit)
        main_layout.addWidget(self.sendButton)
        self.setLayout(main_layout)

    @pyqtSlot()
    def send_msg(self):
        text = self.showEdit.toPlainText()
        self.showEdit.setText(text + '\n' + self.sendEdit.toPlainText())
        ClientService().send_msg_to_friend(self.user['user_id'], self.user['friend_id'], self.sendEdit.toPlainText())
        self.sendEdit.clear()
        print(self.user)