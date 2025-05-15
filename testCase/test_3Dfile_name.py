import os
import random
import time
import json


# 将文件夹中所有同名文件改为规定格式，同时修改json里filename值与名称一致
def rename_files_and_modify_json(folder_path):
    file_dict = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            if file_extension in ['.pcd', '.json']:
                if file_name not in file_dict:
                    while True:
                        random_num1 = random.randint(1000, 1999)
                        random_num2 = random.randint(9000, 9999)
                        random_num3 = random.randint(1, 10)
                        current_time = time.strftime("%Y%m%d%H%M%S") + str(time.time()).split('.')[1][:3]
                        new_file_name = f"{random_num1}-{random_num2}-{random_num3}-JHOCT001-01-02-03-04-{current_time}"
                        new_file_path = os.path.join(root, new_file_name + file_extension)
                        if not os.path.exists(new_file_path):
                            file_dict[file_name] = new_file_name
                            break
                new_file_name = file_dict[file_name]
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_file_name + file_extension)
                try:
                    os.rename(old_file_path, new_file_path)
                    if file_extension == '.json':
                        # 修改 JSON 文件中的 filename 值
                        try:
                            with open(new_file_path, 'r') as f:
                                data = json.load(f)
                            if 'filename' in data:
                                data['filename'] = new_file_name + '.pcd'
                            with open(new_file_path, 'w') as f:
                                json.dump(data, f, indent=4)  # 使用 indent 参数保持格式
                        except Exception as e:
                            print(f"处理文件 {new_file_path} 时出错: {e}")
                except FileExistsError:
                    print(f"文件 {new_file_path} 已存在，跳过重命名。")


folder_path = input("请输入文件夹路径：")
rename_files_and_modify_json(folder_path)