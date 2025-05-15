import os
import json


def replace_json_contents(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        original_data = json.load(f)
                        target_content = {
                            "label": "ng",
                            "cls": "",
                            "score": 0,
                            "imagePath": original_data["imagePath"]
                        }
                    with open(file_path, 'w') as f:
                        json.dump(target_content, f, indent=4)
                    print(f"已成功替换文件: {file_path}")
                except Exception as e:
                    print(f"替换文件 {file_path} 时出错: {e}")


folder_path = r"C:\Users\admin\Desktop\ng"
replace_json_contents(folder_path)
