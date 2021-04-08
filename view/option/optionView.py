from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class OptionView(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.button1 = QPushButton('Welcome', self)
        self.button1.move(230, 120)
        self.button1.clicked.connect(self.welcome)
        self.quitbutton1 = QPushButton('exit', self)
        self.quitbutton1.move(230, 200)
        self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

    def welcome(self):
        self.master.setCurrentIndex(
            self.master.tabIndexDict["process"]
        )
