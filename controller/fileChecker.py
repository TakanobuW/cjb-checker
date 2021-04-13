import os
import numpy as np
import json
import time
from abc import ABC, ABCMeta, abstractmethod
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from PyQt5.QtCore import QObject, pyqtSignal


class FileChecker:
    def __init__(self):
        self.header_len = 10
        self.restore_key_idx = 8

        self.result = []

    def checkFile(self, file_path):
        with open(file_path, mode="rb") as fp:
            bin_data = fp.read()

        file_info = {}
        file_info["fname"] = os.path.basename(file_path).replace(".cjb", "")
        file_info["bytes"] = len(bin_data)

        # 作成日時の取得
        date_bin_data = bin_data[:9]
        date_fmt_str = "{:02d}{:02d}-{:02d}{:02d}-{:02d}:{:02d}:{:02d}:{:02d}{:02d}"
        file_info["date"] = date_fmt_str.format(
            *list(map(lambda x: int(x), date_bin_data)))

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


class MyMeta(ABCMeta, type(QObject)):
    pass


class RunChecker(QObject, metaclass=MyMeta):
    """
    xxx
    """

    # threadからシグナルを飛ばすためのクラス変数(クラス変数じゃないとダメらしい)
    progressChanged = pyqtSignal(int)
    timeChanged = pyqtSignal(str)
    checkEnd = pyqtSignal(List)

    def __init__(self, browserPath, file_path_list):
        super().__init__()

        self.browserPath = browserPath
        self.file_path_list = file_path_list

    def _launchBrowser(self):
        # self.driver = webdriver.Chrome("/usr/bin/chromedriver")
        if self.browserPath is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome(self.browserPath)

        # ドライバーの設定
        self.driver.set_window_size(800, 450)
        self.driver.implicitly_wait(1)  # 各要素を取得する際に最大指定時間繰り返し探索する

        self.driver.get(
            "https://haru1843.github.io/circuit-simulation-app/usage")
        WebDriverWait(self.driver, 5).until(
            (EC.presence_of_element_located((By.ID, "ul-button"))))  # アップロードボタンが現れるまで

        self.file_upload_button = self.driver.find_element_by_id("ul-button")

    def checkFiles(self):
        self._launchBrowser()

        result_list = [{}] * len(self.file_path_list)

        start_time = time.time()
        time_str_fmt = "{:02d}m{:02d}s : {:02d}m{:02d}s"
        for nth, file_path in enumerate(self.file_path_list):
            result_list[nth] = self._checkFile(file_path)
            self.progressChanged.emit(
                ((nth + 1) / len(self.file_path_list)) * 100)

            elapsed_second = time.time() - start_time
            remain_second = (elapsed_second / (nth+1)) * \
                (len(self.file_path_list) - (nth+1))
            elapsed_second = round(elapsed_second)
            remain_second = round(remain_second)
            self.timeChanged.emit(time_str_fmt.format(
                elapsed_second // 60, elapsed_second % 60,
                remain_second // 60, remain_second % 60
            ))

        self.checkEnd.emit(result_list)

        self.driver.close()
        self.driver.quit()

    @abstractmethod
    def _checkFile(self, file_path: str) -> Dict:
        pass

    def getResult(self):
        return self.result

    def closeDriver(self):
        self.driver.close()
        self.driver.quit()


class RunChecker4Work1(RunChecker):
    def __init__(self, browserPath, file_path_list):
        super().__init__(browserPath, file_path_list)

    def _checkFile(self, file_path: str) -> Dict:
        result_dict = {}
        self.file_upload_button.send_keys(file_path)

        circuit = self.driver.find_element_by_css_selector(
            'g[simcir-transform-y="0"]:not(.simcir-scrollbar-bar, .simcir-scrollbar)')

        switches = circuit.find_elements_by_class_name(
            "simcir-basicset-switch")

        if len(switches) != 3:
            print("課題2です.")
            return
        else:
            print("課題1です.")

        button_list = [switch.find_element_by_class_name(
            "simcir-basicset-switch-button") for switch in switches]

        # !!!!!!!!!!!!!!!! ボタンの位置移動する !!!!!!!!!!!!!!!!!!! (translateを移動すればたぶんok)

        # 全部のボタンをオフにする
        for btn in button_list:
            if "simcir-basicset-switch-button-pressed" in btn.get_attribute("class"):
                btn.click()

        # 7seg取得
        device_list = circuit.find_elements_by_class_name("simcir-device")
        target_idx = 0
        for idx, device in enumerate(device_list):
            if len(device.find_elements_by_class_name("simcir-node-type-in")) == 8:
                target_idx = idx
                break
                # device.screenshot("7seg.png")

        # 7segの状態取得
        seven_seg_node_list: List = device_list[target_idx].find_elements_by_class_name(
            "simcir-node-type-in")

        # 7segのinput-nodeを昇順にソート
        seven_seg_node_list.sort(key=lambda x: int(x.get_attribute("simcir-transform-y")))

        # 7segの状態を取得する関数
        def get_7seg_state():
            segment_mapping_list = [
                'ooooooxx',
                'xooxxxxx',
                'ooxooxox',
                'ooooxxox',
                'xooxxoox',
                'oxooxoox',
                'oxooooox',
                'oooxxoxx',
            ]

            try:
                return segment_mapping_list.index("".join(["o" if "simcir-node-hot" in node.get_attribute("class") else "x" for node in seven_seg_node_list]))
            except ValueError:
                return -1

        # ボタンをクリック(0->7), 7segの状態を取得
        click_btn_idx_list = [0, 1, 2, 1, 0, 1, 2]
        btn_state = [0, 0, 0]
        mapping_btn2seg = {
            "{:d}{:d}{:d}".format(*btn_state): get_7seg_state(),
        }

        for click_btn_idx in click_btn_idx_list:
            btn_state[click_btn_idx] = (btn_state[click_btn_idx] + 1) % 2
            button_list[click_btn_idx].click()
            time.sleep(0.1)
            mapping_btn2seg["{:d}{:d}{:d}".format(*btn_state)] = get_7seg_state()

        print(mapping_btn2seg)

        return mapping_btn2seg


class RunChecker4Work2(RunChecker):
    def __init__(self, browserPath, file_path_list):
        super().__init__(browserPath, file_path_list)

    def _checkFile(self, file_path: str) -> Dict:
        self.file_upload_button.send_keys(file_path)
