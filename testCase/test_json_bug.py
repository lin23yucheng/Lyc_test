import os
import json
from pathlib import Path


def count_qipao_labels(folder_path):
    total_count = 0
    if not os.path.exists(folder_path):
        print(f"错误：文件夹 '{folder_path}' 不存在")
        return total_count

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    # 关键修改：解析根对象中的 "shapes" 数组
                    if isinstance(data, dict) and 'shapes' in data:
                        shapes = data['shapes']
                        for item in shapes:
                            if isinstance(item, dict) and item.get('label') == 'qipao':
                                total_count += 1

                except json.JSONDecodeError:
                    print(f"警告：文件 '{file_path}' 不是有效的JSON格式，已跳过")
                except Exception as e:
                    print(f"警告：处理文件 '{file_path}' 时出错: {e}，已跳过")
    return total_count


if __name__ == "__main__":
    folder_path = input("请输入文件夹路径: ").strip()
    if not folder_path:
        print("错误：文件夹路径不能为空")
    else:
        count = count_qipao_labels(folder_path)
        print(f"在文件夹 '{folder_path}' 中，label字段为'qipao'的总数是: {count}")