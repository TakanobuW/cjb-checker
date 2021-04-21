from PyQt5.QtWidgets import QTabWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

# from .option.optionViews import Target, Runtime, Result, Log
from .option import optionViews
from .select import selectViews
from .process import processView
from .log import logViews
from .end import endView


class App(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CJBチェッカー")

        # self.quitbutton1 = QPushButton('exit', self)
        # self.quitbutton1.move(230, 200)
        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

        # オプション
        self.option = {}

        # 対象ファイルのパス
        self.file_path_list = []

        # チェックの結果
        self.file_check_result = []
        self.run_check_result = []

        # 各ページのインスタンス化
        self.tab0 = optionViews.WholeOption(self)
        # self.tab0 = optionViews.Target(self)
        # self.tab1 = optionViews.Runtime(self)
        # self.tab2 = optionViews.Check(self)
        # self.tab3 = optionViews.BrowserPath(self)

        self.tab4 = selectViews.FileSelect(self)
        self.tab5 = selectViews.FolderSelect(self)

        self.tab6 = processView.FileCheckProcessView(self)
        self.tab7 = processView.RunCheckProcessView(self)

        self.tab8 = logViews.Log4File(self)
        self.tab9 = logViews.Log4Run(self)

        self.tab10 = endView.End(self)

        # タブに各ページを追加
        self.addTab(self.tab0, "option-whole")
        # self.addTab(self.tab0, "option-target")
        # self.addTab(self.tab1, "option-runtime")
        # self.addTab(self.tab2, "option-check")
        # self.addTab(self.tab3, "option-browserPath")
        self.addTab(self.tab4, "select-file")
        self.addTab(self.tab5, "select-folder")
        self.addTab(self.tab6, "process-file")
        self.addTab(self.tab7, "process-run")
        self.addTab(self.tab8, "log-file")
        self.addTab(self.tab9, "log-run")
        self.addTab(self.tab10, "end")

        # 各ページとインデックスの対応表
        self.tab_index_dict = {
            "option": 0,
            "select": {
                "file": 1,
                "folder": 2,
            },
            "process": {
                "file": 3,
                "run": 4,
            },
            "log": {
                "file": 5,
                "run": 6,
            },
            "end": 7
        }

        # タブパネルのボーダーを削除
        self.setStyleSheet("QTabWidget::pane { border: 0; }")

        # タブバーを非表示に(↓をコメントすると動きがわかりやすくなるかも)
        self.tabBar().hide()
        # self.resize(960, 540)
        self.setFixedSize(960, 540)
        self.move(100, 0)
