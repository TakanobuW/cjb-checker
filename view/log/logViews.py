from ..base import BaseWidget


class Log4Run(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="回路の実行結果の出力")
        self.master = parent

    def nextPage(self):
        self.master.option["browserPath"] = None

        if self.master.option["target"] == "files":
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["file"]
            )
        elif self.master.option["target"] == "folders":
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["folder"]
            )
        else:
            print("Unecpected behavior in option-browserPath")
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["folder"]
            )


class Log4File(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ファイル内容の結果の出力")
        self.master = parent

    def nextPage(self):
        self.master.option["browserPath"] = None

        if self.master.option["target"] == "files":
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["file"]
            )
        elif self.master.option["target"] == "folders":
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["folder"]
            )
        else:
            print("Unecpected behavior in option-browserPath")
            self.master.setCurrentIndex(
                self.master.tab_index_dict["select"]["folder"]
            )
