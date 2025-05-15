from configs import config
import requests


class Login_quality:
    def get_token(self):
        url_login = f'{config.svfactory_fat}/qcweb/auth/login'
        login_data = {"phone": "11111111111", "password": "qwe123123"}
        headers = {'content-type': 'application/json'}
        login_res = requests.post(url=url_login, json=login_data, headers=headers).json()
        assert '成功' in login_res['msg']
        login_data = login_res['data']
        token = login_data['token']
        return token
