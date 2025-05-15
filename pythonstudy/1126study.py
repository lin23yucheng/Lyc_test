str1 = 'HelloPython,HelloJava,Hellophp'
char = input('请输入要统计的字符：')
char1 = char.upper()
# if str.count(char) > 0:
#     print(str.count(char))
# else:
#     print('无')
print('{0}不区分大小写在"{1}"一共出现了{2}次'.format(char, str1, str1.upper().count(char1)))











