from PyQt5.QtWidgets import QLineEdit


class QQInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setTextMargins(10, 0, 0, 0)
        self.setMaximumWidth(240)
