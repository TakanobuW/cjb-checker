from PyQt5.QtWidgets import QApplication, QWidget
from view.join import Widget
import sys


def main():
    app = QApplication([])
    widget = Widget()
    widget.run()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
