from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
# from PyQt5.QtCore import QCoreApplication


class MyMeta(ABCMeta, type(QWidget)):
    pass


class BaseWidget(QWidget, metaclass=MyMeta):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.master = parent

        self.next_button = QPushButton('次へ', self)
        self.next_button.move(745, 495)
        self.next_button.clicked.connect(self.nextPage)

        title_css = "QLabel { font-size: 30px }"
        title_pos = [30, 30]

        self.title = QLabel(title, self)
        self.title.move(*title_pos)
        self.title.setStyleSheet(title_css)

    def disableNextButton(self):
        self.next_button.setEnabled(False)

    def enableNextButton(self):
        self.next_button.setEnabled(True)

    def hideNextButton(self):
        self.next_button.hide()

    @abstractmethod
    def nextPage(self):
        pass
