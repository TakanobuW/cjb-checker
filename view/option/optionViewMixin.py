from PyQt5.QtWidgets import QPushButton, QGridLayout, QLabel


class OptionViewMixin():
    def optionView(self):
        # buttonの設定
        self.button = QPushButton('Clear!!')
        self.label = QLabel('connected')

        # buttonのclickでラベルをクリア
        self.button.clicked.connect(self.label.clear)

        # レイアウト配置
        self.grid = QGridLayout()
        self.grid.addWidget(self.button, 0, 0, 1, 1)
        self.grid.addWidget(self.label, 1, 0, 1, 2)
        self.setLayout(self.grid)
