# a = 10
# b = 20
#
# print(a, b)
#
# a, b = b, a  # 交换两个变量的值
# print(a, b)
#
# print('-' * 30)
#
# print(98 > 90)
# print(98 < 90)
# print(98 > 90 or 98 < 90)
# print(98 > 90 and 100 < 91)
# print(8 > 7 or 10 / 0)
# print(not True)
# print(not False)
#
# print('-' * 30)

# g = input('输一个四位数：')
# print(type(g))
# # g = int(g)
# # print(type(g))
# #
# # print('个位数字为：', g % 10)
# # print('十位数字为：', g // 10 % 10)
# # print('百位数字为：', g // 100 % 10)
# # print('千位数字为：', g // 1000 % 10)
#
# print('个位数字为：', g[-1])
# print('十位数字为：', g[-2])
# print('百位数字为：', g[-3])
# print('千位数字为：', int(g[0]))

# dad = float(input('请输入爸爸身高：'))
# mom = float(input('请输入妈妈身高：'))
#
# son = (dad + mom) * 0.54
# print('预测儿子身高为：', round(son,2))


# number = eval(input('请输入六位中奖号码：'))
# luck_number = 121900
#
# if luck_number == number:
#     print('恭喜您，中奖啦！')
# else:
#     print('很遗憾， 未中奖。')

# number = eval(input('请输入一位中奖号码：'))
#
# if number == 1:
#     print('恭喜您，一等奖！')
# elif number == 2:
#     print('恭喜您，二等奖！')
# elif number == 3:
#     print('恭喜您，三等奖！')
# else:
#     print('很遗憾， 未中奖。')

# for i in 'cheng':
#     print(i)

# a = 0
# for i in range(1, 101):
#     a += i
# print(a)
#
# for i in range(100, 1000):
#     if (i % 10) ** 3 + (i // 10 % 10) ** 3 + (i // 100) ** 3 == i:
#         print(i, '水仙花数')
#     else:
#         pass

# answer = input('今天上课否?y/n')
# while answer == 'y':
#     print('好好上课')
#     answer = input('今天上课否?y/n')

# s = 0
# i = 0
# while i <= 100:
#     s += i
#     i += 1
# print(s)

# s = 0
# i = 0
# while i <= 100:
#     s += i
#     i += 1
# else:
#     print(s)

use_name = 'cheng'
password = '123'
num = 1

while num <= 3:
    use = input('请输入用户名：')
    pwd = input('请输入密码：')
    if use == use_name and pwd == password:
        print('登录成功')
        break
    else:
        if num < 3:
            print('用户名或密码错误，您还有', 3 - num, '次机会')
        num += 1

if num == 4:
    print('已输入三次错误，账号已锁定！')

# i = 1
# while i <= 3:
#     print('****')
#     i += 1
#
# i = 1
# while i <= 5:
#     if i == 1:
#         print('*')
#         i += 1
#     elif i == 2:
#         print('**')
#         i += 1
#     elif i == 3:
#         print('***')
#         i += 1
#     elif i == 4:
#         print('****')
#         i += 1
#     elif i == 5:
#         print('*****')
#         i += 1


for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='')
    print()

print('--------------------')

# for j in range(1, 6):
#     print("*" * j)

for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()

print('--------------------')

for i in range(1, 6):
    for j in range(1, 7 - i):
        print('*', end='')
    print()

print('--------------------')

for i in range(1, 6):
    for g in range(1, 6 - i):
        print(' ', end='')
    for j in range(1, 2 * i):
        print('*', end='')
    print('')

print('--------------------')

for i in range(1, 5):
    for g in range(1, 5 - i):
        print(' ', end='')
    for j in range(1, i * 2):
        print('*', end='')
    print('')
for a in range(1, 4):
    for b in range(1, a + 1):
        print(' ', end='')
    for c in range(1, 2 * 3 - 2 * a + 2):
        print('*', end='')
    print('')

print('--------------------')

# 输入菱形的行数
row = eval(input('请输入菱形的行数：'))
while row % 2 == 0:
    row = eval(input('请重新输入菱形的行数：'))

# 输出菱形上半部分的行数
top_up = (row + 1) // 2

for i in range(1, top_up + 1):
    for g in range(1, top_up + 1 - i):
        print(' ', end='')
    for j in range(1, i * 2):
        print('*', end='')
    print('')

# 菱形下半部分
top_down = row // 2

for a in range(1, top_down + 1):
    for b in range(1, a + 1):
        print(' ', end='')
    for c in range(1, 2 * top_down - 2 * a + 2):
        print('*', end='')
    print('')

print('--------------------')

# 输入菱形的行数
row = eval(input('请输入菱形的行数：'))
while row % 2 == 0:
    row = eval(input('请重新输入菱形的行数：'))

# 输出菱形上半部分的行数
top_up = (row + 1) // 2

for i in range(1, top_up + 1):
    for g in range(1, top_up + 1 - i):
        print(' ', end='')
    for j in range(1, i * 2):
        if j == 1 or j == i * 2 - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# 菱形下半部分
top_down = row // 2

for a in range(1, top_down + 1):
    for b in range(1, a + 1):
        print(' ', end='')
    for c in range(1, 2 * top_down - 2 * a + 2):
        if c == 1 or c == 2 * top_down - 2 * a + 2 - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')


