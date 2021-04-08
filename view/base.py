from PyQt5.QtWidgets import QWidget


class Base(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.resize(750, 750)
        self.move(300, 300)
        self.setWindowTitle("sample")
        self.show()
