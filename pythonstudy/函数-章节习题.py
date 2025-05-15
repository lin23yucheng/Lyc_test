import random


def lst_max(lst):
    lst2 = sorted(lst)
    min_num = lst2[0]
    print(min_num)
    x = lst[0]
    for i in range(1, len(lst)):
        if x < lst[i]:
            x = lst[i]
    return x


lst = []
i = 0
while i < 10:
    num = random.randint(1, 100)
    lst.append(num)
    i += 1

print(lst)

max = lst_max(lst)
print(max)

# str = input('请输入一个字符串：')
# print(type(str))
# lst = []
# for i in range(len(str)):
#     if str[i].isdigit():
#         lst.append(int(str[i]))
# print('提取的数字列表为：', lst)
#
# sum = 0
# for j in range(len(lst)):
#     sum += lst[j]
# print('累加和为：', sum)


# def get_digit(x):
#     s = 0
#     lst = []
#     for i in x:
#         if i.isdigit():
#             lst.append(int(i))
#
#     s = sum(lst)
#     return lst, s
#
#
# str = input('请输入一个字符串：')
#
# lst, x = get_digit(str)
# print('提取的数字列表为：', lst)
# print('累加和为：', x)

print('---' * 20)


def abc(x, lst):
    for i in lst:
        if x == i:
            return True
    return False


lst = ['a', 'b', 'c']
s = input('请输入一个字符串：')
result = abc(s, lst)

print('存在' if result else '不存在')

if result:
    print('存在')
else:
    print('不存在')
