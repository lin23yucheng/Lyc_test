s1 = 'HelloWorld'

s2 = s1.lower()

s3 = s1.upper()

print(s1, s2, s3)

e_mail = 'linyucheng@qq.com'

lst = e_mail.split('@')

print('邮箱名：', lst[0], '域名：', lst[1])

print(e_mail.count('n'))

print(e_mail.find('c'))

print(e_mail.find('a'))

print(e_mail.startswith('l'))  # True ， 判断开头

print(e_mail.startswith('y'))

print('123.jpg'.endswith('.jpg'))  # True ， 判断结尾

print('123.jpg'.endswith('.jpeg'))

new_s = s1.replace('o', '哈')
print(new_s)

print(s1.center(20, '*'))

s = '     lin   yu   cheng          '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s1.strip('eeHldw'))
print(s.strip(' li'))

print('---' * 20)

name = '林禹成'
age = 30
score = 98.57

print('姓名：%s，年龄：%d，分数：%.2f' % (name, age, score))

print(f'姓名：{name}，年龄：{age}，分数：{score}')

print('姓名：{0}，年龄：{1}，分数：{2}'.format(name, age, score))

print('---' * 20)

s = 'HelloWorld'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))
print(s.center(20, '*'))

print('{0:,}'.format(123456789))
print('{0:,}'.format(987654321.123456789))

print('{0:.2f}'.format(987654321.123456789))

print('{0:.5}'.format('helloworld'))  # 最大显示长度

print('---' * 20)

# 验证数据的正确性

# 所有字符都是十进制数字
print('123'.isdigit())  # True
print('一二三'.isdigit())  # False
print('Ⅰ'.isdigit())  # False

print('---' * 20)

# 所有字符都是数字
print('123'.isnumeric())  # True
print('一二三'.isnumeric())  # True
print('Ⅰ'.isnumeric())  # True

print('---' * 20)

# 所有字符都是字母（包含中文字符）
print('hello你好'.isalpha())  # True
print('hello你好123'.isalpha())  # False
print('hello你好Ⅰ'.isalpha())  # False
print('hello你好一二三'.isalpha())  # True

print('---' * 20)

# 所有字符都是数字或字母
print('hello你好'.isalnum())  # True
print('hello你好123'.isalnum())  # True
print('hello你好Ⅰ'.isalnum())  # True
print('hello你好一二三'.isalnum())  # True

print('---' * 20)

# 判断字符的大小写
print('HelloWorld'.islower())  # False
print('helloworld'.islower())  # True
print('hello你好'.islower())  # True 中文既是大写也是小写
print('---' * 20)
print('HelloWorld'.isupper())  # False
print('HELLOWORLD'.isupper())  # True
print('HELLO你好'.isupper())  # True 中文既是大写也是小写

print('---' * 20)

# 所有字符只能是首字母大写
print('Hello'.istitle())  # True
print('HelloWorld'.istitle())  # False
print('Helloworld'.istitle())  # True
print('Hello World'.istitle())  # True
print('Hello world'.istitle())  # False

print('---' * 20)

# 判断是否都是空白字符
print('\t'.isspace())  # True
print('\n'.isspace())  # True
print(' '.isspace())  # True

print('---' * 20)

s1 = 'hello'
s2 = 'world'

print(s1 + s2)

print(''.join([s1, s2]))

print('+'.join(['python', 'java', 'js']))

print('hello''world')

print('%s%s' % (s1, s2))

print('{0}{1}'.format(s1, s2))

print(f'{s1}{s2}')

# 字符串去重

s = 'helloworldlinyuchenghahakeyide'

new_s = ''

for i in s:
    if i not in new_s:
        new_s += i
print(new_s)

new_s2 = ''

for a in range(len(s)):
    if s[a] not in new_s2:
        new_s2 += s[a]
print(new_s2)

print('---' * 20)

# 正则表达式

import re

a = '\d\.\d+'
s = 'abc3.14def'

b = re.match(a, s, re.I)
print(b)

s2 = '3.1415abcdef'
c = re.match(a, s2, re.I)
print(c)

print('匹配的起始位置：', c.start())
print('匹配的结束位置：', c.end())
print('匹配区间的位置元素：', c.span())
print('待匹配的字符串：', c.string)
print('匹配的数据：', c.group())

print('---' * 20)

a2 = '\d\.\d+'
s2 = 'abc3.14def849236.000haha'

b2 = re.search(a2, s2)
print(b2)
print(b2.group())

b3 = re.findall(a2, s2)
print(b3)
print(b3[1])

print('---' * 20)

a3 = '黑客|破解|收费'
s3 = '我想学习python，破解一些收费软件'
c3 = re.sub(a3, 'xxx', s3)
print(c3)

a4 = '[?|&]'
s4 = 'https://modao.cc/proto/WMeYkU2Usdx6jpNXQpifd/sharing?view_mode=device&screen=rbpUTzrhaS7fYUq7t&canvasId=rcUUYBI6UUYBZuPTXv9hAV'
c4 = re.split(a4, s4)
print(c4)

print('---' * 20)
