from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

from ..base import BaseWidget


class FileCheckProcessView(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ファイル内容の確認")
        self.master = parent

        self.add_button = QPushButton('実行', self)
        self.add_button.move(450, 430)
        self.add_button.clicked.connect(self.execute_check)

        self.hideNextButton()

    def execute_check(self):
        pass

    def nextPage(self):
        if self.master.option["check"]["run"]:
            self.master.setCurrentIndex(
                self.master.tab_index_dict["process"]["run"]
            )
        else:
            self.master.setCurrentIndex(
                self.master.tab_index_dict["result"]
            )


class RunCheckProcessView(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="回路の動作確認中...")
        self.master = parent

        self.add_button = QPushButton('実行', self)
        self.add_button.move(450, 430)
        self.add_button.clicked.connect(self.execute_check)

        self.hideNextButton()

    def execute_check(self):
        pass

    def nextPage(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["result"]
        )
