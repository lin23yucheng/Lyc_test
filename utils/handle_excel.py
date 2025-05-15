import xlrd
import json


def get_excel_data(file_path, sheet_name, case_name):
    # 存放结果
    res_list = []
    # 1.文件在磁盘---读取到---内存
    # formatting_info = True --- 保持原样式
    work_book = xlrd.open_workbook(file_path, formatting_info=True)
    # 获取所有的表名
    # print(work_book.sheet_names())
    # 2.选择对应的sheet
    work_sheet = work_book.sheet_by_name(sheet_name)
    # # 获取一行数据
    # print(work_sheet.row_values(0))
    # # 获取一列数据
    # print(work_sheet.col_values(0))
    # # 单元格数据
    # print(work_sheet.cell(0, 0).value)

    # 获取需要的数据
    row_index = 1  # 行业编号初始值
    for one in work_sheet.col_values(0):
        if case_name in one:
            # 请求体
            req_body = work_sheet.cell(row_index, 2).value
            exp_data = work_sheet.cell(row_index, 3).value
            case_id = work_sheet.cell(row_index, 1).value
            # [(req_body1,exp_data1),(req_body2exp_data2)]
            # 转字典
            res_list.append((json.loads(req_body), json.loads(exp_data), case_id))
            # res_list.append((req_body, exp_data))
            row_index += 1
    # 列表里面包含元组
    return res_list


if __name__ == '__main__':
    res = get_excel_data('../data/登录.xls', '登录', 'login')
    print(res)
