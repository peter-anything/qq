from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit

from widgets.qq_input import QQInput

class QQMain(QWidget):
    def __init__(self, *args, **kwargs):
        super(QQMain, self).__init__(*args, **kwargs)
        # self.setAttribute(Qt.WA_StyledBackground, True)
        main_layout = QVBoxLayout(self)

        title_layout = QHBoxLayout(self, spacing=0)
        title_layout.setContentsMargins(0, 0, 0, 0)

        title_layout_btn1 = QLabel("我的好友", self)
        title_layout_btn1.setObjectName('test')

        title_layout_btn2 = QLabel("我的消息", self)
        title_layout_btn3 = QLabel("我的空间", self)

        title_layout.addWidget(title_layout_btn1)
        title_layout.addWidget(title_layout_btn2)
        title_layout.addWidget(title_layout_btn3)
        title_layout.addStretch()

        content_layout = QVBoxLayout(self)

        for i in range(5):
            user_input = QQInput()
            user_input.setPlaceholderText('peter1')
            content_layout.addWidget(user_input)

        main_layout.addLayout(title_layout)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)