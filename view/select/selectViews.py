from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QRadioButton,
    QLabel,
    QFileDialog,
    QScrollArea,
    QVBoxLayout,
    QListWidget
)
from PyQt5.QtCore import QCoreApplication, Qt
from typing import List, Set

from ..base import BaseWidget


class SelectedList(QListWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self._path_list = set([])
        self._updateView()

        self.itemClicked.connect(self._removePath)

    def addPath(self, path: str):
        self._path_list.add(path)
        self._updateView()

    def _updateView(self):
        self.clear()
        self.addItems(self._path_list)

    def clearPath(self):
        self._path_list = set([])
        self._updateView()

    def _removePath(self, target_item):
        target_idx = self.row(target_item)

        _ = self.takeItem(target_idx)
        # item = None

        self._path_list.discard(target_item.text())
        self._updateView()

    def getPathList(self) -> Set[str]:
        return self._path_list


class FileSelect(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ファイルの選択")
        self.master = parent

        self.add_button = QPushButton('対象ファイルを追加', self)
        self.add_button.move(450, 430)
        self.add_button.clicked.connect(self.showFileDialog)

        self.selected_list = SelectedList(self)
        self.selected_list.resize(860, 300)
        self.selected_list.move(50, 100)

    def showFileDialog(self):
        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        path = QFileDialog.getOpenFileName(self, '対象ファイルの選択', '/home', filter="*.cjb")
        if path[0] != "":
            self.selected_list.addPath(str(path[0]))

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

        self.add_button = QPushButton('対象フォルダを追加', self)
        self.add_button.move(450, 430)
        self.add_button.clicked.connect(self.showFileDialog)

        self.selected_list = SelectedList(self)
        self.selected_list.resize(860, 300)
        self.selected_list.move(50, 100)

    def showFileDialog(self):
        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        path = str(QFileDialog.getExistingDirectory(self, '対象フォルダの選択', '/home'))
        self.selected_list.addPath(path)

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
