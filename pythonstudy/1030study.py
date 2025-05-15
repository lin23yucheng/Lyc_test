# # 创建字典
# d = {10: 'cat', 20: 'dog', 30: "pig", 10: 'zoo'}
# print(d)
#
# # zip函数
# lst1 = [10, 20, 30, 40]
# lst2 = ['cat', 'dog', "pig", 'zoo', 'good']
# zipobj = zip(lst1, lst2)
# print(zipobj)
#
# d = dict(zipobj)
# print(d)
#
# # 使用参数创建字典
#
# d = dict(cat=10, dog=20)
# print(d)
#
# print('---' * 20)
#
# d = {'use': 'cheng', 'pwd': 123, 'role': 'test'}
# print(d['pwd'])
# print(d.get('role'))
#
# # print(d['haha'])
# print(d.get('haha'))
# print(d.get('haha', '无对应值'))
#
# for i in d.items():
#     print(i)
#
# for key, value in d.items():
#     print(key, '--->', value)
#
# print('---' * 20)
#
# # 集合
# s = {'good', 11, 90}
# print(s)
#
# g = set('1234')
# print(g)
#
# g.add('100')
# print(g)
#
# g.remove('3')
# print(g)
#
# # g.clear()
# # print(g)
#
# for i in g:
#     print(i)
#
# print('---' * 20)
#
# # lst = [88, 89, 90, 98, 00, 99]
# # lst1 = []
# # print(lst)
# #
# # for i in lst:
# #     if i != 0:
# #         i = 1900 + i
# #     elif i == 0:
# #         i = 2000 + i
# #     lst1.append(i)
# #     print(i)
# # print(lst1)
#
# lst = [88, 89, 90, 98, 00, 99]
# lst1 = []
# print(lst)
#
# for i in lst:
#     if i != 0:
#         i = '19' + str(i)
#     elif i == 0:
#         i = '200' + str(i)
#     lst1.append(i)
# print(lst1)
#
# for index in range(len(lst)):
#     if lst[index] != 0:
#         lst[index] = '19' + str(lst[index])
#     else:
#         lst[index] = '200' + str(lst[index])
# print(lst)
#
# print('---' * 20)

# lst = []
# i = 1
# while i <= 5:
#     product = input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品：')
#     lst.append(product)
#     i += 1
# # print(lst)
# for i in lst:
#     print(i)
#
# cart = []
# while True:
#     flag = False
#     num = input('请输入要购买的商品编号:')
#     for i in lst:
#         if num == i[0:4]:
#             flag = True
#             cart.append(i[4:])
#             print('商品已添加到购物车')
#             break
#     if not flag and num != 'q':
#         print('商品不存在')
#     if num == 'q':
#         break
# print('---' * 20)
# print('购物车已选择的商品为：')
# cart.reverse()
# for i in cart:
#     print(i)

# print('---' * 20)

# lst = [
#     ['车次', '出发站-到达站', '出发时间','到达时间间隔','历时时长'],
#     ['G1569', '北京南-天津南', '18：06','18:39','00:33'],
#     ['G1567', '北京南-天津南', '18：15','18:49','00:34'],
#     ['G8917', '北京南-天津西', '18：20','19:19','00:59'],
#     ['G203', '北京南-天津南', '18：35','19:09','00:34']
# ]
#
# for a in lst:
#     for b in a:
#         print(b, end='\t')
#     print()

list = [1, 2, 3, "a", "你好"]

for i in range(len(list)):
    print(list[i])
