from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt


class End(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent

        title_css = "QLabel { font-size: 30px }"

        self.title = QLabel("完了", self)
        self.title.move(150, 230)
        self.title.setFixedWidth(660)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(title_css)

        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)
