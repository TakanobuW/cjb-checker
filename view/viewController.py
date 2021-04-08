from PyQt5.QtWidgets import QTabWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

# from .option.optionViews import Target, Runtime, Result, Log
from .option import optionViews
from .select import selectViews
from .process.processView import ProcessView


class App(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello")

        # self.quitbutton1 = QPushButton('exit', self)
        # self.quitbutton1.move(230, 200)
        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

        # 各ページのインスタンス化
        self.tab0 = optionViews.Target(self)
        self.tab1 = optionViews.Runtime(self)
        self.tab2 = optionViews.Check(self)
        self.tab3 = optionViews.BrowserPath(self)
        self.tab4 = selectViews.FileSelect(self)
        self.tab5 = selectViews.FolderSelect(self)

        # タブに各ページを追加
        self.addTab(self.tab0, "option-target")
        self.addTab(self.tab1, "option-runtime")
        self.addTab(self.tab2, "option-check")
        self.addTab(self.tab3, "option-browserPath")
        self.addTab(self.tab4, "select-file")
        self.addTab(self.tab5, "select-folder")

        # 各ページとインデックスの対応表
        self.tab_index_dict = {
            "option": {
                "target": 0,
                "runtime": 1,
                "check": 2,
                "browserPath": 3,
            },
            "select": {
                "file": 4,
                "folder": 5,
            },
            "process": 6,
        }

        # オプション
        self.option = {}

        # タブパネルのボーダーを削除
        self.setStyleSheet("QTabWidget::pane { border: 0; }")

        # タブバーを非表示に(↓をコメントすると動きがわかりやすくなるかも)
        self.tabBar().hide()
        self.resize(960, 540)
        self.move(100, 0)
