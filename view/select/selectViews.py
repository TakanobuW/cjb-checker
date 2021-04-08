from PyQt5.QtWidgets import QWidget, QPushButton, QRadioButton, QLabel, QCheckBox
from PyQt5.QtCore import QCoreApplication

from ..base import BaseWidget


class FileSelect(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ファイルの選択")
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


class FolderSelect(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="フォルダの選択")
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
