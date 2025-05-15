a = 100
b = 50

print(20)
print(a / b)
print('可以')
print(20, a * b, 'haha')

print(chr(26519))
print(ord('成'))

print('前', end='-->')
print('后')

# name = input('请输入姓名：')
# age = input('请输入年龄：')
# print('--------自我介绍--------')
# print('姓名：' + name)
# print('年龄：' + age)


import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

a = 0.1
b = 0.2
print(round(a + b, 1), a, b)

print(int(3.14))

s = '3.14+2'
print(s, type(s))

print('-----')

x = eval(s)
print(x, type(x))

q = 23
w = 3
z = q / w
print(round(z, 2))
print(round(z))

print(int(z * 100) / 100)

x = 225 / 9
print(x)
s = 45 / x * 5
print(s)
