from PyQt5.QtWidgets import QWidget, QPushButton, QRadioButton, QLabel
from PyQt5.QtCore import QCoreApplication

from ..base import BaseWidget


class Target(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="選択方法の設定")
        self.master = parent

        self.rbtn_files = QRadioButton("ファイル単位", self)
        self.rbtn_files.move(175, 180)
        self.rbtn_folders = QRadioButton("フォルダー単位", self)
        self.rbtn_folders.move(175, 310)

        self.rbtn_folders.setChecked(True)

    def nextPage(self):
        if self.rbtn_files.isChecked():
            self.master.option["target"] = "files"
            # print(self.rbtn_files.text())
        elif self.rbtn_folders.isChecked():
            self.master.option["target"] = "folders"
            # print(self.rbtn_folders.text())
        else:
            print("Unecpected behavior in option-target")
            self.master.option["target"] = "folders"

        self.master.setCurrentIndex(
            self.master.currentIndex() + 1
        )


class Runtime(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="実行時の設定")
        self.master = parent

        self.rbtn_speed = QRadioButton("速度重視", self)
        self.rbtn_speed.move(175, 180)
        self.rbtn_accurate = QRadioButton("正確さ重視", self)
        self.rbtn_accurate.move(175, 310)

        self.rbtn_accurate.setChecked(True)

    def nextPage(self):

        if self.rbtn_speed.isChecked():
            self.master.option["runtime"] = "speed"
        elif self.rbtn_accurate.isChecked():
            self.master.option["runtime"] = "accurate"
        else:
            print("Unecpected behavior in option-runtime")
            self.master.option["runtime"] = "accurate"

        self.master.setCurrentIndex(
            self.master.currentIndex() + 1
        )


class Result(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="結果の表示設定")
        self.master = parent

        self.cb
        self.rbtn_files = QRadioButton("a", self)
        self.rbtn_files.move(175, 180)
        self.rbtn_folders = QRadioButton("b", self)
        self.rbtn_folders.move(175, 310)

        self.rbtn_folders.setChecked(True)

    def nextPage(self):
        if self.rbtn_files.isChecked():
            print(self.rbtn_files.text())

        if self.rbtn_folders.isChecked():
            print(self.rbtn_folders.text())

        self.master.setCurrentIndex(
            self.master.currentIndex() + 1
        )
