from PyQt5.QtWidgets import QWidget, QPushButton, QRadioButton, QLabel, QCheckBox
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
        elif self.rbtn_folders.isChecked():
            self.master.option["target"] = "folders"
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


class Check(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="確認項目の設定")
        self.master = parent

        self.cb_file_check = QCheckBox("ファイル内容の確認", self)
        self.cb_file_check.move(175, 180)
        self.cb_file_check.stateChanged.connect(self.checkBoxChangedAction)
        self.cb_run_check = QCheckBox("回路の動作確認", self)
        self.cb_run_check.move(175, 310)
        self.cb_run_check.stateChanged.connect(self.checkBoxChangedAction)

        self.rbtn_work1 = QRadioButton("課題1", self)
        self.rbtn_work1.move(200, 360)
        self.rbtn_work2 = QRadioButton("課題2", self)
        self.rbtn_work2.move(200, 390)

        self.cb_file_check.setChecked(True)
        self.cb_run_check.setChecked(True)
        self.rbtn_work1.setChecked(True)

    def checkBoxChangedAction(self, state):
        if (not self.cb_file_check.isChecked()) and (not self.cb_run_check.isChecked()):
            self.disableNextButton()
        else:
            self.enableNextButton()

        if self.cb_run_check.isChecked():
            self.rbtn_work1.setEnabled(True)
            self.rbtn_work2.setEnabled(True)
        else:
            self.rbtn_work1.setEnabled(False)
            self.rbtn_work2.setEnabled(False)

    def nextPage(self):
        self.master.option["check"] = {
            "file": False,
            "run": False,
        }

        if self.cb_file_check.isChecked():
            self.master.option["check"]["file"] = True
        else:
            self.master.option["check"]["file"] = False

        if self.cb_run_check.isChecked():
            self.master.option["check"]["run"] = True

            if self.rbtn_work1.isChecked():
                self.master.option["check"]["run-target"] = "work1"
            elif self.rbtn_work2.isChecked():
                self.master.option["check"]["run-target"] = "work2"
            else:
                print("Unecpected behavior in option-check")
                self.master.option["check"]["run-target"] = "work1"
        else:
            self.master.option["check"]["run"] = False

        self.master.setCurrentIndex(
            self.master.currentIndex() + 1
        )


class BrowserPath(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ブラウザのパス設定")
        self.master = parent

    def nextPage(self):
        self.master.option["browserPath"] = None

        if self.master.option["target"] == "files":
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["file"]
            )
        elif self.master.option["target"] == "folders":
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["folder"]
            )
        else:
            print("Unecpected behavior in option-browserPath")
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["folder"]
            )
