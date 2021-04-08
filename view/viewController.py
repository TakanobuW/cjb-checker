from PyQt5.QtWidgets import QTabWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

# from .option.optionViews import Target, Runtime, Result, Log
from .option import optionViews
from .process.processView import ProcessView


class App(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello")

        # self.quitbutton1 = QPushButton('exit', self)
        # self.quitbutton1.move(230, 200)
        # self.quitbutton1.clicked.connect(QCoreApplication.instance().quit)

        # 各ページのインスタンス化
        self.tab1 = optionViews.Target(self)
        self.tab2 = optionViews.Runtime(self)
        self.tab3 = optionViews.Result(self)

        # タブに各ページを追加
        self.addTab(self.tab1, "option-target")
        self.addTab(self.tab2, "option-runtime")
        self.addTab(self.tab3, "option-result")

        # 各ページとインデックスの対応表
        self.tab_index_dict = {
            "option": 0,
            "process": 1,
        }

        # オプション
        self.option = {}

        # タブパネルのボーダーを削除
        self.setStyleSheet("QTabWidget::pane { border: 0; }")

        # self.master_next_button.setStyleSheet("QPushButton { background-color: white }")

        # タブバーを非表示に(↓をコメントすると動きがわかりやすくなるかも)
        self.tabBar().hide()
        self.resize(960, 540)
        self.move(100, 0)

    def master_next_page(self):
        print(self.currentIndex())
        self.setCurrentIndex((self.currentIndex()+1) % len(self.tab_index_dict))

    def piyo_piyo(self, text):
        print(text)
