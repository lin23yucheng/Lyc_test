import os
import zipfile
import cv2
import numpy as np


def process_folder(folder_path):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(('.jpg', '.png', '.jpeg')):
                image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
                if image is not None and len(image.shape) >= 3 and image.shape[2] == 4:
                    new_image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
                    cv2.imwrite(file_path, new_image)
                    count += 1
    return count



folder_path = r'C:\Users\admin\Desktop\上传测试\四通道\ng'  # 替换为实际的文件夹路径
converted_count = process_folder(folder_path)
print(f"已转为三通道（原为四通道）的图片数量为：{converted_count}")
