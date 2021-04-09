import os
import numpy as np


class FileChecker:
    def __init__(self):
        self.result = []

    def readFile(self, file_path):
        with open(file_path, mode="rb") as fp:
            bin_data = fp.read()

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
