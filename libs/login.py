import requests
from configs import config
from utils.handle_data import get_md5_data
import json


# 封装 登录类
class Login:
    # 封装登录接口
    def login(self, body_data):
        # 1.请求的url
        url_login = f'{config.svfactory_fat}/qcweb/auth/login'
        # 2.请求头
        headers = {'content-type': 'application/json'}
        # 3.请求body
        # # md5加密
        # body_data['password'] = get_md5_data(body_data['password'])
        payload = body_data
        # 4.发送请求
        resp = requests.post(url=url_login, json=payload, headers=headers)
        # deta:使用场景 --- 在请求头里面的type-表单格式
        #     -表单格式 from--- a=1&b=2
        #     -表单里有json from--- a=1&b={"name":"lyc"}
        # 5.返回响应数据为字符串类型
        # return resp.text
        return resp.json()


if __name__ == '__main__':
    test_data = {"phone": "11111111111", "password": "qwe123123"}
    # 1.使用类去创建实例
    login = Login()
    # 2.调用登录接口
    res = login.login(test_data)
    print(res)
    user_list = res['data']
    print(user_list)
    token = user_list['token']
    print(token)
