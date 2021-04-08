from PyQt5.QtWidgets import QTabWidget

from .option.optionView import OptionView
from .process.processView import ProcessView


class App(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")

        # 各ページのインスタンス化
        self.tab1 = OptionView(self)
        self.tab2 = ProcessView(self)

        # タブに各ページを追加
        self.addTab(self.tab1, "StartMenu")
        self.addTab(self.tab2, "WelcomeMenu")

        # 各ページとインデックスの対応表
        self.tabIndexDict = {
            "option": 0,
            "process": 1,
        }

        # タブパネルのボーダーを削除
        self.setStyleSheet("QTabWidget::pane { border: 0; }")
        # タブバーを非表示に(↓をコメントすると動きがわかりやすくなるかも)
        self.tabBar().hide()
        self.resize(500, 300)
        self.move(100, 0)

    def piyo_piyo(self, text):
        print(text)
