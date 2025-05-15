import os
import random
import time
import json

def rename_files_and_modify_json(folder_path):
    file_groups = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            if file_extension in ['.jpg', '.json']:
                base_name = file_name.rsplit('-pre', 1)[0]
                if base_name not in file_groups:
                    file_groups[base_name] = [file]
                else:
                    file_groups[base_name].append(file)

    for base_name, file_list in file_groups.items():
        random_num = random.randint(10, 100)
        current_time = time.strftime("%Y%m%d%H%M%S") + str(time.time()).split('.')[1][:3]
        new_file_name = f"0003-0001-{random_num}-WXOCT001-01-01-01-01-{current_time}"
        for file in file_list:
            old_file_path = os.path.join(root, file)
            if file.endswith('-pre.json'):
                new_file_path = os.path.join(root, new_file_name + '-pre.json')
            else:
                new_file_path = os.path.join(root, new_file_name + os.path.splitext(file)[1])
            try:
                os.rename(old_file_path, new_file_path)
            except Exception as e:
                print(f"重命名文件时出现错误：{e}")

            if file.endswith('.json'):
                with open(new_file_path, 'r') as f:
                    data = json.load(f)
                    if 'imagePath' in data:
                        data['imagePath'] = new_file_name + '.jpg'
                with open(new_file_path, 'w') as f:
                    try:
                        json.dump(data, f)
                    except Exception as e:
                        print(f"写入 JSON 文件时出现错误：{e}")

folder_path = input("请输入文件夹路径：")
rename_files_and_modify_json(folder_path)