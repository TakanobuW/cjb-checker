from ..base import BaseWidget
import os
import json

from PyQt5.QtWidgets import QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt


class LogBaseWidget(BaseWidget):
    def __init__(self, parent, title):
        super().__init__(parent, title)
        self.master = parent

        self.save_path_str = QLabel(self)
        self.save_path_str.move(150, 200)
        self.save_path_str.setAlignment(Qt.AlignCenter)
        self.save_path_str.setFixedWidth(660)
        self.save_path_str.setText("選択なし")
        self.save_path_str.setStyleSheet(
            "QLabel { font-size: 14px; border: 1px solid gray; border-radius: 5px; background-color: white; }")

        self.select_btn = QPushButton('保存先を選択する', self)
        self.select_btn.move(430, 250)
        self.select_btn.clicked.connect(self.showFileDialog)

        self.save_btn = QPushButton('結果を保存する', self)
        self.save_btn.move(430, 400)
        self.save_btn.setEnabled(False)
        self.save_btn.clicked.connect(self.saveFile)

        self.file_saved = False

    def saveFile(self):
        result_json = json.dumps(self.master.file_check_result, indent=2)
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'template', 'work1_result_template.html'), mode="r") as fp:
            output_html = \
                fp.read() + \
                f"<script>const run_result_json = `{result_json}`</script>"

        open(os.path.join(self.save_path_str.text(), "work1_result.html"), mode="w").write(output_html)
        open(os.path.join(self.save_path_str.text(), "work1_result.json"), mode="w").write(result_json)
        self.file_saved = True
        QMessageBox.information(None, "通知", "ファイルの保存が完了しました.", QMessageBox.Ok)

    def showFileDialog(self):
        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        path = str(QFileDialog.getExistingDirectory(self, '保存先フォルダの選択', '/home'))
        if path != "":
            self.save_path_str.setText(path)
            self.save_btn.setEnabled(True)


class Log4File(LogBaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ファイル内容の結果の出力")
        self.master = parent

    def nextPage(self):
        if not self.file_saved:
            result = QMessageBox.question(None, "確認", "ファイルに保存せず次に進みますか？",
                                          QMessageBox.Yes, QMessageBox.No)

        if self.file_saved or (result == QMessageBox.Ok):
            if self.master.option["check"]["run"]:
                self.master.setCurrentIndex(
                    self.master.tab_index_dict["log"]["run"]
                )
            else:
                self.master.setCurrentIndex(
                    self.master.tab_index_dict["end"]
                )


class Log4Run(LogBaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="回路の実行結果の出力")
        self.master = parent

    def nextPage(self):
        self.master.setCurrentIndex(
            self.master.tab_index_dict["end"]
        )
