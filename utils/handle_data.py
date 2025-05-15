# 函数需求：MD5加密操作
# 入参：加密的明文
# 出参：加密的密文
import hashlib


def get_md5_data(pwd: str):
    # 1.实例化md5对象
    md5 = hashlib.md5()
    # 2.调用加密操作
    md5.update(pwd.encode('UTF-8'))
    # 3.返回加密后的结果，16进制
    return md5.hexdigest()
