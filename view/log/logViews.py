from ..base import BaseWidget


class Log4File(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ファイル内容の結果の出力")
        self.master = parent

    def nextPage(self):
        if self.master.option["check"]["run"]:
            self.master.setCurrentIndex(
                self.master.tab_index_dict["log"]["run"]
            )
        else:
            self.master.setCurrentIndex(
                self.master.tab_index_dict["end"]
            )


class Log4Run(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="回路の実行結果の出力")
        self.master = parent

    def nextPage(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["end"]
        )
