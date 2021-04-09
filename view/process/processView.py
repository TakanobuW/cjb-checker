from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class FileCheckProcessView(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent


class RunCheckProcessView(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
