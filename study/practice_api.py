# 1.基类common  baseAPI封装
#     ---一个业务模块：增删改查
#     ---后续的所有业务都可以继承这个基类
# 2.libs：业务层
# 3.configs 配置
#     ---环境的数据   项目url
# 4.data 数据层
#     ---测试用例
#       -excel用例
#       -yaml用例
# 5.用例层
# 6.工具包


import requests
import re
import datetime

fat = 'https://fat-brain-gw.svfactory.com.cn:6143'

# # # 获取13位时间戳
# # t = round(time.time()*1000)
# # print(t)
#
# 获取当前时间到毫秒
now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
# print(now)

# 企业工单新增
url_add = fat + '/svc/issue/svc/add'

data_add = {"issueType": "企业工单", "compName": "python公司名称" + now, "demandType": "2", "demandTitle": "python工单标题" + now,
            "demandDesc": "python工单描述" + now}

headers = {'content-type': 'application/json'}

res_add = requests.post(url=url_add, json=data_add, headers=headers)

print(res_add.text)

# 企业工单新增后的查询
url_page = fat + '/svc/issue/svc/page'

data_page = {"data": {"demandTitle": "", "demandType": "", "issueType": "企业工单"},
             "page": {"pageIndex": 1, "pageSize": 10}}

res_page = requests.post(url=url_page, json=data_page, headers=headers)
# 转json
print(res_page.json())
# 取所有list
data_list = res_page.json()["data"]["list"]
print(data_list)
# 遍历list中带有变量now的数据
for i in data_list:
    if i["compName"].find(now) != -1:
        print(i)
        data = i
# 取遍历出来数据的工单编号
work_order_id = data['issueNo']
print(work_order_id)

# # 提取排序第一的工单id值
# re_dict = res_page.json()
# id_data = re_dict['data']
# id_list = id_data['list']
# id_page = id_list[0]
# work_order_id = id_page['issueNo']
# print(work_order_id)

# # search正则，group取第一个小括号的值
# pattern = r'"issueNo":"(\d+)","issueType":"企业工单","compName":"python公司名称' + now + '"'
# print(pattern)
# id_get = re.search(pattern, res_page.text)
# print(id_get)
# work_order_id = id_get.group(1)
# print(work_order_id)

# findall正则，取list第一个值
# pattern2 = '"issueNo":"(\d+)","issueType":"企业工单","compName":"python公司名称' + now + '"'
# print(pattern2)
# id_get2 = re.findall(pattern2, res_page.text)
# print(id_get2)
# work_order_id = id_get2[0]
# print(work_order_id)

# 删除企业刚新增的工单
url_delete = fat + '/svc/issue/svc/delete'

data_delete = {"ids": [work_order_id]}

res_delete = requests.post(url=url_delete, json=data_delete, headers=headers)

print(res_delete.text)

# 再次查询企业工单
url_page = fat + '/svc/issue/svc/page'

data_page = {"data": {"demandTitle": "", "demandType": "", "issueType": "企业工单"},
             "page": {"pageIndex": 1, "pageSize": 10}}

res_page = requests.post(url=url_page, json=data_page, headers=headers)

print(res_page.text)
