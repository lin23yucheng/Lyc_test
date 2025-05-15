def get_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    print(f'1-{n}的累加和为：{s}')


get_sum(1)
get_sum(10)
get_sum(100)
get_sum(1000)
get_sum(10000)

