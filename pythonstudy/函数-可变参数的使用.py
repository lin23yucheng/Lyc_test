def fun(*pare):
    print(type(pare))
    for i in pare:
        print(i)


fun(10, 20, 30, 40, 50)
fun(10)
fun([11, 22, 33])
fun(*[11, 22, 33])  # 解包


def fun2(**kpara):
    print(type(kpara))
    for key, value in kpara.items():
        print(key, '-----', value)


fun2(name='LYC', age=30, height=174)
