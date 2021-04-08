# from PyQt5.QtWidgets import QApplication, QWidget
# from view.join import Widget
# import sys


# def main():
#     app = QApplication([])
#     widget = Widget()
#     widget.run()

#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()

# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication

from view.viewController import App


def main():
    app = QApplication(sys.argv)
    appWidget = App()
    appWidget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
