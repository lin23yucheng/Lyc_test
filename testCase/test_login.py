from libs.login import Login
from utils.handle_excel import get_excel_data
import pytest
import allure
import os


class TestLogin:
    # 数据驱动
    @pytest.mark.parametrize('req_body,exp_data,case_id', get_excel_data('../data/登录.xls', '登录', 'login'))
    def test_login(self, req_body, exp_data, case_id):
        # 调用登录接口
        res = Login().login(req_body)
        # 响应=断言
        # assert res['msg'] == exp_data['msg']
        # 包含
        assert exp_data['msg'] in res['msg']


if __name__ == '__main__':
    # -s 打印输入
    # -sq简化输入
    # # pytest.main([__file__, '-s'])

    pytest.main(['-s', "test_login.py", "--alluredir=../report/allure_result"])
    # 将report目录下生成的json数据转换成html测试报告文件
    os.system("allure generate ../report/allure_result -o ../report/html_result/ --clean")
    # 打开报告,本机地址+自定义端口
    # os.system("allure open -h 127.0.0.1 -p 8883 ../report/html_result")
