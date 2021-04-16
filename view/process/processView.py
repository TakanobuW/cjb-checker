from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QLabel,
    QProgressBar,
    QAbstractItemView
)
from PyQt5.QtCore import QCoreApplication, Qt, QThread, pyqtSlot
from PyQt5.QtGui import QColor


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
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
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
                self.master.tab_index_dict["log"]["file"]
            )


class RunCheckProcessView(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="回路の動作確認")
        self.master = parent

        self.run_button = QPushButton('実行', self)
        self.run_button.move(450, 490)
        self.run_button.clicked.connect(self.executeCheck)

        self.remain_time_msg = QLabel(self)
        self.remain_time_msg.setAlignment(Qt.AlignCenter)
        self.remain_time_msg.move(150, 230)
        self.remain_time_msg.setFixedWidth(660)
        self.remain_time_msg.setText("経過時間 : 予測残り時間")
        self.remain_time_msg.setStyleSheet("QLabel { font-size: 22px }")

        self.progress = QProgressBar(self)
        self.progress.setGeometry(100, 280, 760, 25)
        self.progress.setMaximum(100)

        self.table = QTableWidget(self)
        self.table.hide()

        self.disableNextButton()

        self.thread = QThread(self)

    def checkEndAction(self, result_list):
        self.enableNextButton()

        # keys = list(result_list[0].keys())
        keys = ["fname", "workability", "error-details", "mapping"]
        self.table.setRowCount(len(result_list))
        self.table.setColumnCount(len(keys))
        self.table.setHorizontalHeaderLabels(keys)
        for nth, result in enumerate(result_list):
            for key_idx, key in enumerate(keys):
                self.table.setItem(nth, key_idx, QTableWidgetItem(str(result[key])))
                if not result["workability"]:
                    self.table.item(nth, key_idx).setBackground(QColor(245, 160, 157))

        self.master.run_check_result = result_list

        self.table.move(50, 70)
        self.table.resize(860, 400)
        self.table.setSortingEnabled(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.show()

        if self.thread.isRunning():
            self.thread.terminate()

    def executeCheck(self):
        self.run_button.hide()

        # チェックする課題に応じてインスタンスを生成
        if self.master.option["check"]["run-target"] == "work1":
            self.checker = RunChecker4Work1(
                browser_path=self.master.option["browserPath"],
                file_path_list=self.master.file_path_list,
                implicitly_wait_time=self.master.option["runtime"]["implicitly_wait"],
                click_wait_time=self.master.option["runtime"]["click_wait"]
            )
        elif self.master.option["check"]["run-target"] == "work2":
            self.checker = RunChecker4Work2(
                browser_path=self.master.option["browserPath"],
                file_path_list=self.master.file_path_list,
                implicitly_wait_time=self.master.option["runtime"]["implicitly_wait"],
                click_wait_time=self.master.option["runtime"]["click_wait"]
            )
        else:
            print("Unecpected behavior in process-run")
            self.checker = RunChecker4Work1(
                browser_path=self.master.option["browserPath"],
                file_path_list=self.master.file_path_list,
                implicitly_wait_time=self.master.option["runtime"]["implicitly_wait"],
                click_wait_time=self.master.option["runtime"]["click_wait"]
            )

        # メインの方の描画更新がとまってしまうため,
        # インスタンスをスレッド化し, 別スレッドにて実行
        self.checker.moveToThread(self.thread)
        self.thread.started.connect(self.checker.checkFiles)
        self.checker.progressChanged.connect(self.progress.setValue, Qt.QueuedConnection)
        self.checker.timeChanged.connect(self.remain_time_msg.setText, Qt.QueuedConnection)
        self.checker.checkEnd.connect(self.checkEndAction, Qt.QueuedConnection)

        self.thread.start()

    def nextPage(self):
        if self.master.option["check"]["file"]:
            self.master.setCurrentIndex(
                self.master.tab_index_dict["log"]["file"]
            )
        else:
            self.master.setCurrentIndex(
                self.master.tab_index_dict["log"]["run"]
            )
