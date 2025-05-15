import pytest
import allure
import os
import datetime
from libs.login import *
import requests
from configs import config
from libs.login_quality import Login_quality

now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
token = Login_quality().get_token()
print(token)
print(type(token))


# @allure.feature('角色权限模块')
# class Test_role:
#     @allure.story('新增角色权限')
#     def test_add_role(self):
#         url_add = f'{config.svfactory_fat}/qcweb/qcroles/add'
#         add_data = {"name": now + "python接口", "permissions": [{"id": "1"}, {"id": "2"}]}
#         res_add = requests.post(url=url_add, json=add_data, headers=token)
#         print(res_add)


if __name__ == '__main__':
    pass
    # login = Test_role()
    # res = login.test_add_role()
    # print(res)
    # pytest.main(['-s', "test_quality.py", "--alluredir=../report/allure_result"])
    # 将report目录下生成的json数据转换成html测试报告文件
    # os.system("allure generate ../report/allure_result -o ../report/html_result/ --clean")
    # 打开报告,本机地址+自定义端口
    # os.system("allure open -h 127.0.0.1 -p 8883 ../report/html_result")
