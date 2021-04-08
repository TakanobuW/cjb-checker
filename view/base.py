from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
# from PyQt5.QtCore import QCoreApplication


class MyMeta(ABCMeta, type(QWidget)):
    pass


class BaseWidget(QWidget, metaclass=MyMeta):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.master = parent

        self.master_next_button = QPushButton('次へ', self)
        self.master_next_button.move(745, 495)
        self.master_next_button.clicked.connect(self.nextPage)

        title_css = "QLabel { font-size: 30px }"
        title_pos = [30, 30]

        self.title = QLabel(title, self)
        self.title.move(*title_pos)
        self.title.setStyleSheet(title_css)

        # self.rbtn_folders.setChecked(True)

        # self.button1 = QPushButton('Option', self)
        # self.button1.move(230, 120)
        # self.button1.clicked.connect(self.welcome)

        # self.quitbutton1 = QPushButton('exit', self)
        # self.quitbutton1.move(230, 200)
        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

    @abstractmethod
    def nextPage(self):
        pass
        # print(self.currentIndex())
        # self.setCurrentIndex((self.currentIndex()+1) % len(self.tab_index_dict))
