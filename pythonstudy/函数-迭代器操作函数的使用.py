lst = [23, 45, 3, 643, 2345, 234, 12, 456]

# 排序操作
asc_lst = sorted(lst)
desc_lst = sorted(lst, reverse=True)

print(lst)
print(asc_lst)
print(desc_lst)

# reversed 反向
new_lst = reversed(lst)
print(type(new_lst))
print(list(new_lst))

# zip
x = ['a', 'b', 'c']
y = [11, 21, 31, 41, 51, 61]

zipobj = zip(x, y)

print(type(zipobj))

# print(list(zipobj))

# enumerate
enum = enumerate(y, start=1)
print(type(enum))
print(tuple(enum))

# all
lst2 = [10, 20, '', 30]
print(all(lst2))
print(all(lst))

# any
print(any(lst2))

# next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))


# filter
def fun(num):
    return num % 2 == 1


obj = filter(fun, range(10))
print(list(obj))


# map
def asd(x):
    return x.upper()


new_lst2 = ['hello', 'world']
obj2 = map(asd, new_lst2)
print(list(obj2))
