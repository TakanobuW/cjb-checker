from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QCoreApplication

from ..base import BaseWidget

from controller.fileChecker import FileChecker


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
            checker.readFile(file_path=path)

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
        super().__init__(parent, title="回路の動作確認中...")
        self.master = parent

        self.run_button = QPushButton('実行', self)
        self.run_button.move(450, 430)
        self.run_button.clicked.connect(self.executeCheck)

        self.hideNextButton()

    def executeCheck(self):
        print(self.master.file_path_list)

        if self.master.option["check"]["run-target"] == "work1":
            pass
        elif self.master.option["check"]["run-target"] == "work2":
            pass
        else:
            print("Unecpected behavior in process-run")
            pass

    def nextPage(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["result"]
        )
