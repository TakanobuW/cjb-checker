from ..base import BaseWidget
import os
import json
from abc import abstractmethod

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

    @abstractmethod
    def saveFile(self):
        pass

    def showFileDialog(self):
        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        path = str(QFileDialog.getExistingDirectory(
            self, '保存先フォルダの選択', '/home'))
        if path != "":
            self.save_path_str.setText(path)
            self.save_btn.setEnabled(True)


class Log4File(LogBaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title="ファイル内容の結果の出力")
        self.master = parent

    def saveFile(self):
        result_json = json.dumps(self.master.file_check_result, indent=2)
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'template', 'file_result_template.html'), encoding="utf-8", mode="r") as fp:
            output_html = \
                fp.read() + \
                f"<script>const run_result_json = `{result_json}`</script>"

        open(os.path.join(self.save_path_str.text(), "file_result.html"),
             encoding="utf-8", mode="w").write(output_html)
        open(os.path.join(self.save_path_str.text(), "file_result.json"),
             encoding="utf-8", mode="w").write(result_json)
        self.file_saved = True
        QMessageBox.information(None, "通知", "ファイルの保存が完了しました.", QMessageBox.Ok)

    def nextPage(self):
        if not self.file_saved:
            result = QMessageBox.question(None, "確認", "ファイル内容のデコード結果をファイルに出力せずに進みますか？",
                                          QMessageBox.Yes, QMessageBox.No)

        if self.file_saved or (result == QMessageBox.Yes):
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

    def saveFile(self):
        subdir_name = "mapping"

        relative_subpath_list = [os.path.join(".", subdir_name, f"{nth}.html")
                                 for nth in range(len(self.master.run_check_result))]

        # windows だと aタグに不適切なファイルパスになるため,,,,
        a_tag_href_list = [
            "/".join([".", subdir_name, f"{nth}.html"]) for nth in range(len(self.master.run_check_result))]

        main_result_json = json.dumps(
            [{**r, "link": f"<a href=\'{p}\'>クリック</a>"}
                for r, p in zip(self.master.run_check_result, a_tag_href_list)],
            indent=2)
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'template', 'run_result_template.html'), encoding="utf-8", mode="r") as fp:
            output_html = \
                fp.read() + \
                f"<script>const run_result_json = `{main_result_json}`</script>"

        open(os.path.join(self.save_path_str.text(), "run_result.html"),
             encoding="utf-8", mode="w").write(output_html)
        json.dump(
            self.master.run_check_result,
            open(os.path.join(self.save_path_str.text(),
                 "run_result.json"), encoding="utf-8", mode="w"),
            indent=2
        )

        subdir_path = os.path.join(self.save_path_str.text(), subdir_name)
        os.makedirs(subdir_path, exist_ok=True)

        # チェックする課題に応じて読み込むテンプレートを変える
        if self.master.option["check"]["run-target"] == "work1":
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'template', 'work1_mapping_template.html'), encoding="utf-8", mode="r") as fp:
                output_html = fp.read()
        elif self.master.option["check"]["run-target"] == "work2":
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'template', 'work2_mapping_template.html'), encoding="utf-8", mode="r") as fp:
                output_html = fp.read()
        else:
            print("Unecpected behavior in log-run")
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'template', 'work1_mapping_template.html'), encoding="utf-8", mode="r") as fp:
                output_html = fp.read()

        for relative_subpath, result in zip(relative_subpath_list, self.master.run_check_result):
            result_json = json.dumps([{"switch-state": k, "segment-state": v}
                                      for k, v in result['mapping'].items()])
            open(os.path.join(subdir_path, os.path.basename(
                relative_subpath)), encoding="utf-8", mode="w").write(
                    output_html +
                f"<script>const run_result_json = `{result_json}`</script>"
            )

        self.file_saved = True
        QMessageBox.information(None, "通知", "ファイルの保存が完了しました.", QMessageBox.Ok)

    def nextPage(self):
        if not self.file_saved:
            result = QMessageBox.question(None, "確認", "回路の実行結果をファイルに出力せずに進みますか?",
                                          QMessageBox.Yes, QMessageBox.No)

        if self.file_saved or (result == QMessageBox.Yes):
            self.master.setCurrentIndex(
                self.master.tab_index_dict["end"]
            )
