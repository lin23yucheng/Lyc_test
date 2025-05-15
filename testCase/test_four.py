import zipfile
import cv2
import numpy as np


def identify_four_channel_images(zip_file_path):
    count = 0
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith(('.jpg', '.png', '.jpeg')):
                with zip_ref.open(file_name) as image_file:
                    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
                    if image is not None:
                        if len(image.shape) >= 3:
                            if image.shape[2] == 4:
                                print(file_name)
                                count += 1
    return count


zip_file_path = r'C:\Users\admin\Desktop\验证集_原始样本_20241021161839.zip'
four_channel_image_count = identify_four_channel_images(zip_file_path)
print(f"四通道图像的数量为：{four_channel_image_count}")
