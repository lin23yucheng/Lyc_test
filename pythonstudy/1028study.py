# s = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         i += 1
#         continue
#     else:
#         s += i
#         i += 1
# print('1-100的偶数和为：', s)

# print('---' * 20)
#
# x = 0
# for i in range(1, 101):
#     if i % 2 == 1:
#         continue
#     else:
#         x += i
# print('1-100的奇数和为：', x)
#
# print('---' * 20)
#
# year = eval(input('请输入四位数年份：'))
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(str(year) + '年是闰年')
#
# else:
#     print(str(year) + '年是平年')
#
# print('---' * 20)
#
# yue = 234.5
# gps = 4
# tell = 101.89
#
# while True:
#     print('----------欢迎使用10086查询系统----------')
#     print('1.查询当前余额')
#     print('2.查询当前的剩余流量')
#     print('3.查询当前剩余的通话时长')
#     print('0.退出系统')
#     num = eval(input('请输入您要执行的操作：'))
#     if num == 1:
#         print('当前余额为：', yue)
#     elif num == 2:
#         print('当前的剩余流量为', gps, 'GB')
#     elif num == 3:
#         print('当前剩余通话时长为', tell, 'min')
#     elif num == 0:
#         break
#     else:
#         print('输入有误，请重新输入')
#
#     ynn = input('还继续操作吗？y/n')
#     if ynn == 'y':
#         continue
#     elif ynn == 'n':
#         break
#     else:
#         print('输入有误，请重新输入')
#

# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, '*', i, '=', j * i, end='\t')
#     print('')
#
# print('---' * 20)
#
# # 猜数字
# import random
#
# c = 1
# rang = random.randint(1, 100)
#
# while c <= 10:
#     num = eval(input('请输入我所想之数：'))
#     if rang > num:
#         print('小了，还剩', 10 - c, '次机会')
#     elif rang < num:
#         print('大了，还剩', 10 - c, '次机会')
#     elif rang == num:
#         print('恭喜你，猜对了！')
#         break
#     c += 1
#     if c == 11:
#         print('你输了！')
#         break

# s = 'HelloWorld'
#
# print('e存在么？', ('e' in s))
# print('v存在么？', ('v' in s))
# print('e不存在么？', ('e' not in s))
# print('v不存在么？', ('v' not in s))
#
# print(len(s))
# print(min(s))
# print(max(s))
#
# print(s.index('o'))
# # print(s.index('v'))
#
# print(s.count('o'))


# 列表
# lst = ['a', 'b', 'c', 'd']
#
# for a in lst:
#     print(a)
#
# for i in range(0, len(lst)):
#     print(i, '--->', lst[i])
#
# for index, item in enumerate(lst):
#     print(index, item)

# lst = [45, 245, 63, 6, 26, 83, 27, 4, 7, 36]
#
# print('原列表：', lst)
#
# lst.sort()
# print('升序：', lst)
#
# lst.sort(reverse=True)
# print('降序：', lst)
#
# print('-' * 50)
#
# lst2 = ['apple', 'Banana', 'Bed', 'good', 'kobe', 'Rose']
#
# print('原列表：', lst2)
#
# lst2.sort()
# print('升序：', lst2)
#
# # 忽略大小写进行排序
# lst2.sort(key=str.lower)
# print('升序：', lst2)
#
# # 列表生产式
# import random
#
# lst = [a for a in range(1, 11)]
# print(lst)
#
# lst2 = [random.randint(1, 100) for b in range(1, 11)]
# print(lst2)
#
# lst3 = [i for i in range(1, 11) if i % 2 == 0]
# print(lst3)

lst = [
    ['城市', '净值', '投资'],
    ['北京', 325, 141],
    ['上海', 251, 102]
]

for a in lst:
    for b in a:
        print(b, end='\t')
    print()
#
# lst2 = [[j for j in range(1, 6)] for i in range(1, 5)]
# print(lst2)
# for c in lst2:
#     for d in c:
#         print(d, end='   ')
#     print()

# lst = ['sa', 123, '圣诞节']
# lst.append('hello')
# print(lst)
#
# lst.remove(123)
# print(lst)
# lst.pop(0)
# print(lst)
#
# lst[1]=['Hi']
# print(lst)


