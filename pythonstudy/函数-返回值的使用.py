def sum(a, b):
    s = a + b
    print(s)


sum(10, 20)
print(sum(1, 2))

print('---' * 20)


def sum2(a, b):
    y = a + b
    return y


get_y = sum2(2, 3)
print(get_y)

print('---' * 20)


def get_sum(num):
    s = 0
    odd_sum = 0
    even_sum = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
        s += i
    return s, odd_sum, even_sum


result = get_sum(10)
print(type(result))
print(result)

a, b, c = get_sum(10)  # 解包赋值
print(a)
print(b)
print(c)
