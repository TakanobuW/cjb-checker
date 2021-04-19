from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QRadioButton,
    QLabel,
    QCheckBox,
    QFileDialog,
    QLineEdit,
    QMessageBox,
    QGroupBox,
    QVBoxLayout
)
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QDoubleValidator

from ..base import BaseWidget


class MyMeta(ABCMeta, type(QWidget)):
    pass


class OptionPartWidget(QWidget, metaclass=MyMeta):
    def __init__(self, parent, title, desc):
        super().__init__(parent)
        self.master = parent

        self.resize(480, 210)

        self.vbox = QVBoxLayout()

        self.group_box = QGroupBox(self)
        self.group_box.setTitle("○" + title)
        self.group_box.resize(465, 204)

        # 説明用のラベル\
        self.desc_msg = QLabel(self)
        # self.desc_msg.move(10, 10)
        self.desc_msg.resize(445, 50)
        self.desc_msg.setText(desc)
        self.desc_msg.setStyleSheet("QLabel { color: #404040; font-size: 12px; }")
        self.vbox.addWidget(self.desc_msg)

        self._initInputs()

        # アラート用のラベル
        self.alert_msg = QLabel(self)
        self.vbox.addWidget(self.alert_msg)

        self.group_box.setLayout(self.vbox)

    @abstractmethod
    def _initInputs(self):
        pass

    def _setAlertMsg(self):
        pass

    @abstractmethod
    def _getInputInfoDict(self):
        pass


class TargetOptionPart(OptionPartWidget):
    def __init__(self, parent):
        super().__init__(parent,
                         title="選択方法の設定",
                         desc="ファイルを個別に指定するか, CJBファイルを含むフォルダを指定するかを選択できます.")

    def _initInputs(self):
        self.rbtn_files = QRadioButton("ファイル単位", self)
        self.vbox.addWidget(self.rbtn_files)
        self.rbtn_folders = QRadioButton("フォルダー単位", self)
        self.vbox.addWidget(self.rbtn_folders)

        self.rbtn_folders.setChecked(True)

    def _getInputInfoDict(self):
        rtn_dict = {}

        if self.rbtn_files.isChecked():
            rtn_dict["target"] = "files"
        elif self.rbtn_folders.isChecked():
            rtn_dict["target"] = "folders"
        else:
            print("Unecpected behavior in option-target")
            rtn_dict["target"] = "folders"

        return rtn_dict


class RuntimeOptionPart(OptionPartWidget):
    def __init__(self, parent):
        super().__init__(parent,
                         title="実行時の設定",
                         desc="xxxx")

    def _initInputs(self):
        self.search_wait_time = QLineEdit(self)
        # self.search_wait_time.move(175, 180)
        self.search_wait_time.setValidator(QDoubleValidator(
            0.01, 3.00, 2, notation=QDoubleValidator.StandardNotation))
        self.search_wait_time.setText("0.2")
        self.search_label = QLabel(self)
        self.search_label.setText("各要素探索にかける時間(秒)")
        # self.search_label.move(175, 160)

        self.click_wait_time = QLineEdit(self)
        # self.click_wait_time.move(175, 310)
        self.click_wait_time.setValidator(QDoubleValidator(0.01, 3.00, 2))
        self.click_wait_time.setText("0.1")
        self.click_label = QLabel(self)
        self.click_label.setText("要素をクリック後の待機時間(秒)")
        # self.click_label.move(175, 290)

        self.vbox.addWidget(self.search_wait_time)
        self.vbox.addWidget(self.search_label)
        self.vbox.addWidget(self.click_wait_time)
        self.vbox.addWidget(self.click_label)

    def _getInputInfoDict(self):
        rtn_dict = {
            "runtime": {
                "implicitly_wait": float(self.search_wait_time.text()),
                "click_wait": float(self.click_wait_time.text())
            }
        }

        return rtn_dict


class CheckOptionPart(OptionPartWidget):
    def __init__(self, parent):
        super().__init__(parent,
                         title="確認項目の設定",
                         desc="xxxx")

    def _initInputs(self):
        self.search_wait_time = QLineEdit(self)
        # self.search_wait_time.move(175, 180)
        self.search_wait_time.setValidator(QDoubleValidator(
            0.01, 3.00, 2, notation=QDoubleValidator.StandardNotation))
        self.search_wait_time.setText("0.2")
        self.search_label = QLabel(self)
        self.search_label.setText("各要素探索にかける時間(秒)")
        # self.search_label.move(175, 160)

        self.click_wait_time = QLineEdit(self)
        # self.click_wait_time.move(175, 310)
        self.click_wait_time.setValidator(QDoubleValidator(0.01, 3.00, 2))
        self.click_wait_time.setText("0.1")
        self.click_label = QLabel(self)
        self.click_label.setText("要素をクリック後の待機時間(秒)")
        # self.click_label.move(175, 290)

        self.vbox.addWidget(self.search_wait_time)
        self.vbox.addWidget(self.search_label)
        self.vbox.addWidget(self.click_wait_time)
        self.vbox.addWidget(self.click_label)

    def _getInputInfoDict(self):
        rtn_dict = {
            "runtime": {
                "implicitly_wait": float(self.search_wait_time.text()),
                "click_wait": float(self.click_wait_time.text())
            }
        }

        return rtn_dict


class BrowserOptionPart(OptionPartWidget):
    def __init__(self, parent):
        super().__init__(parent,
                         title="ブラウザパスの設定",
                         desc="xxxx")

    def _initInputs(self):
        self.search_wait_time = QLineEdit(self)
        # self.search_wait_time.move(175, 180)
        self.search_wait_time.setValidator(QDoubleValidator(
            0.01, 3.00, 2, notation=QDoubleValidator.StandardNotation))
        self.search_wait_time.setText("0.2")
        self.search_label = QLabel(self)
        self.search_label.setText("各要素探索にかける時間(秒)")
        # self.search_label.move(175, 160)

        self.click_wait_time = QLineEdit(self)
        # self.click_wait_time.move(175, 310)
        self.click_wait_time.setValidator(QDoubleValidator(0.01, 3.00, 2))
        self.click_wait_time.setText("0.1")
        self.click_label = QLabel(self)
        self.click_label.setText("要素をクリック後の待機時間(秒)")
        # self.click_label.move(175, 290)

        self.vbox.addWidget(self.search_wait_time)
        self.vbox.addWidget(self.search_label)
        self.vbox.addWidget(self.click_wait_time)
        self.vbox.addWidget(self.click_label)

    def _getInputInfoDict(self):
        rtn_dict = {
            "runtime": {
                "implicitly_wait": float(self.search_wait_time.text()),
                "click_wait": float(self.click_wait_time.text())
            }
        }

        return rtn_dict


class WholeOption(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="各種設定の変更")
        self.master = parent

        # 選択方法の設定
        self.option_target = TargetOptionPart(self)
        self.option_target.move(0 + 10, 75 + 4)

        # 実行時の設定
        self.option_runtime = RuntimeOptionPart(self)
        self.option_runtime.move(480 + 5, 75 + 4)

        # 選択方法の設定
        self.option_check = CheckOptionPart(self)
        self.option_check.move(0 + 10, 285 + 2)

        # ブラウザパスの設定
        self.option_browser = BrowserOptionPart(self)
        self.option_browser.move(480 + 5, 285 + 2)

        # self.option_runtime = OptionPartWidget(self, "ブラウザパスの設定", desc="")
        # self.option_runtime.move(480 + 5, 285 + 2)

    def nextPage(self):
        pass


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

        self.search_wait_time = QLineEdit(self)
        self.search_wait_time.move(175, 180)
        self.search_wait_time.setValidator(QDoubleValidator(
            0.01, 3.00, 2, notation=QDoubleValidator.StandardNotation))
        self.search_wait_time.setText("0.2")
        self.search_label = QLabel(self)
        self.search_label.setText("各要素探索にかける時間(秒)")
        self.search_label.move(175, 160)

        self.click_wait_time = QLineEdit(self)
        self.click_wait_time.move(175, 310)
        self.click_wait_time.setValidator(QDoubleValidator(0.01, 3.00, 2))
        self.click_wait_time.setText("0.1")
        self.click_label = QLabel(self)
        self.click_label.setText("要素をクリック後の待機時間(秒)")
        self.click_label.move(175, 290)

    def nextPage(self):
        try:
            self.master.option["runtime"] = {
                "implicitly_wait": float(self.search_wait_time.text()),
                "click_wait": float(self.click_wait_time.text())
            }
        except ValueError:
            QMessageBox.warning(None, "ValueError!", "数値を入力してください.", QMessageBox.Yes)
        else:
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

        self.browser_path_str = QLabel(self)
        self.browser_path_str.move(150, 200)
        self.browser_path_str.setAlignment(Qt.AlignCenter)
        self.browser_path_str.setFixedWidth(660)
        self.browser_path_str.setText("選択なし")
        self.browser_path_str.setStyleSheet(
            "QLabel { font-size: 14px; border: 1px solid gray; border-radius: 5px; background-color: white; }")

        self.select_btn = QPushButton('パスを選択する', self)
        self.select_btn.move(430, 250)
        self.select_btn.clicked.connect(self.showFileDialog)

        self.master.option["browserPath"] = None

    def showFileDialog(self):
        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        # path = QFileDialog.getOpenFileName(self, 'ブラウザの実行可能ファイル選択', '/home', filter="*.cjb")
        path = QFileDialog.getOpenFileName(self, 'ブラウザの実行可能ファイル選択', '/home')
        if path[0] != "":
            self.master.option["browserPath"] = str(path[0])
            self.browser_path_str.setText(path[0])

    def nextPage(self):

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
