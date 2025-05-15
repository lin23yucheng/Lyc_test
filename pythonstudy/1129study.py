# try:
#     num1 = eval(input('请输入一个整数：'))
#     num2 = int(input('请输入另一个整数：'))
#     result = num1 / num2
#     # print(num1, '除以', num2, '结果为：', result)
# except ZeroDivisionError:
#     print('除数不允许为0')
# except  ValueError:
#     print('不允许输入非整数')
# except BaseException:
#     print('未知异常')
# else:
#     print(num1, '除以', num2, '结果为：', result)
# finally:
#     print('程序运行结束!')

print('---' * 20)

# try:
#     gender = input('请输入你的性别：')
#     if gender != '男' and gender != '女':
#         raise Exception('请输入男或者女')
#     else:
#         print('您的性别是：', gender)
# except Exception as e:
#     print(e)

print('---' * 20)

try:
    score = eval(input('请输入分数：'))
    if 0 <= score <= 100:
        print('分数为：', score)
    else:
        raise Exception('分数必须在0-100之间')
except Exception as e:
    print(e)
 