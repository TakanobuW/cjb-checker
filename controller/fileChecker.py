import os
import numpy as np
import json
from abc import ABC, abstractmethod


class FileChecker:
    def __init__(self):
        self.header_len = 10
        self.restore_key_idx = 8

        self.result = []

    def readFile(self, file_path):
        with open(file_path, mode="rb") as fp:
            bin_data = fp.read()

        file_info = {}
        file_info["fname"] = os.path.basename(file_path).replace(".cjb", "")
        file_info["bytes"] = len(bin_data)

        # 作成日時の取得
        date_bin_data = bin_data[:9]
        date_fmt_str = "{:02d}{:02d}-{:02d}{:02d}-{:02d}:{:02d}:{:02d}:{:02d}{:02d}"
        file_info["date"] = date_fmt_str.format(*list(map(lambda x: int(x), date_bin_data)))

        # 復元キーの取得 と デコード(binary->文字列)
        restore_val = date_bin_data[self.restore_key_idx]
        text_bin_data = bytes(
            map(lambda x: x - restore_val if x - restore_val >= 0 else x - restore_val + 256,
                bin_data[self.header_len:])
        )

        # 回路構成部分をJSON文字列からデコード
        circuit = json.loads(text_bin_data.decode("utf-8"))
        file_info["device_num"] = len(circuit["devices"])
        centre = np.array([[device["x"], device["y"]]
                           for device in circuit["devices"]]).mean(axis=0)
        file_info["x_centre"] = centre[0]
        file_info["y_centre"] = centre[1]

        self.result.append(file_info)

    def getResult(self):
        return self.result


class RunChecker(ABC):
    def __init__(self, browserPath):
        self.result = []

        self.click_stop_time = 0.05  # sec

        # self.driver = webdriver.Chrome("/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(browserPath)
        self.driver.set_window_size(800, 450)
        self.driver.implicitly_wait(0.3)

        self.driver.get("https://haru1843.github.io/circuit-simulation-app/usage")
        time.sleep(2)

        # self.file_input_element = self.driver.find_element_by_id("ul-input")

    @abstractmethod
    def readFile(self, file_path: str):
        pass

    def getResult(self):
        return self.result


class RunChecker4Work1(RunChecker):
    def __init__(self, browserPath):
        super().__init__(browerPath)

    def readFile(self, file_path: str):
        pass


class RunChecker4Work2(RunChecker):
    def __init__(self, browserPath):
        super().__init__(browerPath)

    def readFile(self, file_path: str):
        pass
