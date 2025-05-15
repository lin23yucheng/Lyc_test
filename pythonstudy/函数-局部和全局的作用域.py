a = 100


def fun(x, y):
    return a + x + y


print(a)
print(fun(10, 20))

print('---' * 20)


def fun2(x, y):
    a = 200
    return a + x + y


print(fun2(10, 20))
print(a)

print('---' * 20)


def fun3(x, y):
    global s
    s = 300
    global a
    a = x + y
    return s + x + y, a


print(fun3(10, 20))
print(s)
print(a)
