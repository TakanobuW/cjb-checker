from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class Target(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent

        # self.button1 = QPushButton('Option', self)
        # self.button1.move(230, 120)
        # self.button1.clicked.connect(self.welcome)

        # self.quitbutton1 = QPushButton('exit', self)
        # self.quitbutton1.move(230, 200)
        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

    def welcome(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["process"]
        )


class Runtime(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent

        # self.button1 = QPushButton('Option', self)
        # self.button1.move(230, 120)
        # self.button1.clicked.connect(self.welcome)

        # self.quitbutton1 = QPushButton('exit', self)
        # self.quitbutton1.move(230, 200)
        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

    def welcome(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["process"]
        )


class Result(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent

        # self.button1 = QPushButton('Option', self)
        # self.button1.move(230, 120)
        # self.button1.clicked.connect(self.welcome)

        # self.quitbutton1 = QPushButton('exit', self)
        # self.quitbutton1.move(230, 200)
        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

    def welcome(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["process"]
        )


class Log(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent

        # self.button1 = QPushButton('Option', self)
        # self.button1.move(230, 120)
        # self.button1.clicked.connect(self.welcome)

        # self.quitbutton1 = QPushButton('exit', self)
        # self.quitbutton1.move(230, 200)
        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

    def welcome(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["process"]
        )
