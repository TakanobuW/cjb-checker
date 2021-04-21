from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor
# from PyQt5.QtCore import Qt
# from PyQt5.QtCore import QCoreApplication


class MyMeta(ABCMeta, type(QWidget)):
    pass


class BaseWidget(QWidget, metaclass=MyMeta):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.master = parent

        # ページ遷移用の「次へ」ボタン
        self.next_button = QPushButton('次へ', self)
        self.next_button.move(850, 502)
        self.next_button.clicked.connect(self.nextPage)

        # ページタイトル
        title_css = "QLabel { font-size: 30px }"
        title_pos = [20, 20]
        self.title = QLabel(title, self)
        self.title.move(*title_pos)
        self.title.setStyleSheet(title_css)

    def paintEvent(self, event):
        """
        paintEventをオーバーライド
        """
        # ページタイトル用の帯的な
        painter = QPainter(self)
        painter.setPen(QColor(220, 220, 220))
        painter.setBrush(QColor(220, 220, 220))
        painter.drawRect(0, 0, 960, 75)

    def disableNextButton(self):
        self.next_button.setEnabled(False)

    def enableNextButton(self):
        self.next_button.setEnabled(True)

    def hideNextButton(self):
        self.next_button.hide()

    @abstractmethod
    def nextPage(self):
        pass
