class Student:
    # 类属性：定义在类中，方法外的变量
    school = '上海东方明珠'

    # 初始方法
    def __init__(self, xm, age):  # xm，age是方法的参数，是局部变量；xm，age的作用域是整个__init__方法
        self.name = xm  # 左侧是实例属性，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
        self.age = age  # 实例的名称和局部变量的名称可以相同

    # 定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫{self.name},今年{self.age}岁')


stu1 = Student('A同学', 18)
stu2 = Student('B同学', 19)
stu3 = Student('C同学', 20)

print(Student.school)
Student.school = 'python教育'

# 将学生对象存储到列表中
lst = [stu1, stu2, stu3]  # 列表中的元素是Student类型的对象
for i in lst:  # i是列表中的元素，是Student类型的对象
    i.show()

print(Student.school)
