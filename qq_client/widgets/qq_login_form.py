from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit

from widgets.qq_input import QQInput

class QQLoginForm(QWidget):
    def __init__(self, *args, **kwargs):
        super(QQLoginForm, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        form_layout.setFormAlignment(Qt.AlignHCenter)

        name_input1 = QQInput()
        name_input1.setPlaceholderText('用户名')

        name_input2 = QQInput()
        name_input2.setPlaceholderText('密码')
        name_input2.setEchoMode(QLineEdit.Password)

        login_button = QPushButton()
        login_button.setMaximumWidth(240)
        login_button.setText('登陆')

        # 向布局中添加这几个控件
        form_layout.addRow('', name_input1)
        # 一行两个控件，水平摆放
        form_layout.addRow('', name_input2)
        form_layout.addRow('', login_button)

        hbox2 = QHBoxLayout()  # 水平布局

        hbox2_btn1 = QLabel("注册账号", self)
        hbox2_btn1.setObjectName('test')
        hbox2_btn2 = QLabel("扫码登陆", self)

        hbox2.addWidget(hbox2_btn1)
        hbox2.addStretch()
        hbox2.addWidget(hbox2_btn2)

        form_layout.setContentsMargins(0, 50, 0, 0)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(hbox2)

        self.setLayout(main_layout)