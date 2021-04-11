from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QCoreApplication

from ..base import BaseWidget

from controller.fileChecker import FileChecker, RunChecker4Work1, RunChecker4Work2

from selenium.common.exceptions import TimeoutException


class FileCheckProcessView(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ファイル内容の確認")
        self.master = parent

        self.run_button = QPushButton('実行', self)
        self.run_button.move(450, 490)
        self.run_button.clicked.connect(self.executeCheck)

        self.table = QTableWidget(self)
        self.table.hide()

        self.disableNextButton()

    def executeCheck(self):
        self.run_button.hide()
        checker = FileChecker()

        for nth, path in enumerate(self.master.file_path_list):
            # print(f"{nth+1} / {len(self.master.file_path_list)}")
            checker.checkFile(file_path=path)

        self.master.file_check_result = checker.getResult()
        self.updateTable()
        self.table.move(50, 70)
        self.table.resize(860, 400)
        self.table.setSortingEnabled(True)
        self.table.show()

        self.enableNextButton()

    def updateTable(self):
        keys = list(self.master.file_check_result[0].keys())
        self.table.setRowCount(len(self.master.file_check_result))
        self.table.setColumnCount(len(keys))
        self.table.setHorizontalHeaderLabels(keys)
        for nth, result in enumerate(self.master.file_check_result):
            for key_idx, key in enumerate(keys):
                self.table.setItem(nth, key_idx, QTableWidgetItem(str(result[key])))

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
        super().__init__(parent, title="回路の動作確認")
        self.master = parent

        self.run_button = QPushButton('実行', self)
        self.run_button.move(450, 490)
        self.run_button.clicked.connect(self.executeCheck)

        self.table = QTableWidget(self)
        self.table.hide()

        self.disableNextButton()

    def executeCheck(self):
        self.run_button.hide()

        # チェックする課題に応じてインスタンスを生成
        if self.master.option["check"]["run-target"] == "work1":
            checker = RunChecker4Work1(browserPath=self.master.option["browserPath"])
        elif self.master.option["check"]["run-target"] == "work2":
            checker = RunChecker4Work2(browserPath=self.master.option["browserPath"])
        else:
            print("Unecpected behavior in process-run")
            checker = RunChecker4Work1(browserPath=self.master.option["browserPath"])

        try:
            checker.launchBrowser()
        except TimeoutException as error:
            QMessageBox.warning(None, "TimeoutExceptionエラー", "サイトへの初期接続が遅すぎます.", QMessageBox.Yes)
            self.run_button.show()
            self.run_button.setText("再実行")
            checker.closeDriver()
            return

        for nth, path in enumerate(self.master.file_path_list):
            print(f"{nth+1} / {len(self.master.file_path_list)}")
            checker.checkFile(file_path=path)

        checker.closeDriver()
        self.enableNextButton()

    def nextPage(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["result"]
        )
