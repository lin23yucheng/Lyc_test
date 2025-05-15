import os
import shutil
import random

def copy_and_rename_files(folder_path, num_copies):
    file_groups = {}
    # 先将原始文件分组
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            if file_extension in ['.jpg', '.json']:
                base_name = file_name.rsplit('-pre', 1)[0]
                if base_name not in file_groups:
                    file_groups[base_name] = [os.path.join(root, file)]
                else:
                    file_groups[base_name].append(os.path.join(root, file))

    # 对每组文件进行复制和重命名操作
    for base_name, file_list in file_groups.items():
        for i in range(num_copies):
            # 生成随机的 5 位数字作为前缀
            random_prefix = str(random.randint(10000, 99999))
            new_file_name = random_prefix + '-' + base_name
            for file in file_list:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1]
                if file.endswith('-pre.json'):
                    new_file_path = os.path.join(root, new_file_name + '-pre' + file_extension)
                else:
                    new_file_path = os.path.join(root, new_file_name + file_extension)
                try:
                    # 复制文件
                    shutil.copy2(file_path, new_file_path)
                except Exception as e:
                    print(f"复制文件时出现错误：{e}")

folder_path = input("请输入文件夹路径：")
num_copies = int(input("请输入要复制的份数："))
copy_and_rename_files(folder_path, num_copies)