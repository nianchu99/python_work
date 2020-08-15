from collections.abc import Iterable, Iterator
import os
from functools import reduce
import functools
from PIL import Image

# This is a dict
d = {"chenqiaochu": 1227, "bowenkei": 1223}
# key 迭代
for key in d:
    print("The name is " + str(key))
print()
# value 迭代
for value in d.values():
    print("His/Her birthday is " + str(value))
print()
# key, value同时迭代
for k, v in d.items():
    print("The name is %s, and His/Her birthday is %s " % (k, v))

# 使用collections模块中的Iterable类型判断一个对象是不是可迭代对象
first = isinstance("abc", Iterable)  # str是否可迭代
second = isinstance([1, 2, 3], Iterable)  # list是否可迭代
thrid = isinstance(123, Iterable)  # 整数是否可迭代的
print(first)
print(second)
print(thrid)

# 让list实现下标循环
for i, value in enumerate(["A", 'B', 'C']):
    print(i, value)

print()
for x, y in [(1, 1), (2, 4), (3, 9), (2, 10), (100, 100)]:
    print(x, y)
# 创建一个set
s = set([1, 2, 3, 4, 5])
print(type(s))
# 列表生成式
list1 = list(range(1, 11))
print(type(list1))
print(list1)
# 高级操作
list2 = [x * x for x in range(1, 11)]
print(list2)
# for循环后面还可以加上if判断，这样可以执行一些筛选
list3 = [x * x for x in range(1, 11) if x % 2 == 0]

# 使用两层循环实现全排列
list4 = [m + n for m in 'ABC' for n in "abc"]

print(type(list3))
print(type(list4))

print(list3)
print(list4)

# 列出当前目录下的所有文件和目录名
list5 = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print(list5)

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
list6 = [k + ' = ' + v for k, v in d.items()]
print(list6)

# 将list中的所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
list7 = [s.lower() for s in L]
print(type(list7))
print(list7)

# Exercise
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(type(L2))
print(L2)

# 创建一个最简单的generator
G = (x * x for x in range(10))
print(type(G))
# 使用next()函数输出生成器中的元素
for i in range(10):
    print(next(G))

# 使用循环输出
for n in G:
    print(n)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# print(fib(9))
# generator生成的另一种方法
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

    return "done"


# generator生成的另一种方法
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

    return "done, and very good!"


# 使用fib1()函数
for n in fib1(6):
    print(n)
"""
def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 3
    print("step 3")
    yield 5
"""
# 要想捕获到generator中的返回值，需要使用try-except语句
g = fib1(6)
while True:
    try:
        x = next(g)
        print("g: ", x)
    except StopIteration as e:
        print("Generator return value", e.value)
        break


# Exercise 写出一个关于杨辉三角形的generator
def yH(max):
    list9 = []
    list8 = []
    index = 1
    while index < max:
        if index == 1:
            list8 = [1]
            yield list8
            index = index + 1
        elif index == 2:
            list8 = [1, 1]
            yield list8
            index = index + 1
        else:
            list9 = [None] * index
            for I in range(1, index - 1):
                list9[I] = list8[I - 1] + list8[I]
            list9[0] = 1
            list9[index - 1] = 1
            yield list9
            index += 1
            list8 = list9


g1 = yH(11)
for n in g1:
    print(n)

print("Hello world")
print(next(yH(11)))

# 判断一个对象是不是Iterator
print(isinstance((x * x for x in range(10)), Iterator))
print(isinstance(" ", Iterator))

f = abs
print(f(-10))


def add(x, y, f):
    return f(x) + f(y)


print(add(5, -6, abs))


# 将x^2作用到一个list[1, 2, 3, 4, 5, 6, 7, 9]上，可以使用map()
# 定义函数
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 9])
'''
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))'''
# 由上面的几条print语句可以看出map函数得到的是一个Iterator
print(list(r))


# 关于reduce的用法
# 实现累加
def add(x, y):
    return x + y


redce_detail = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(redce_detail)


# 实现将一个序列中的所有数字变成一个整数
def changeToInteger(x, y):
    return x * 10 + y


list_for_str = [1, 2, 3, 4, 5, 6, 7]
integer = reduce(changeToInteger, list_for_str)
print(integer)


# 使用reduce和map()函数，写出将str转换为int的函数：
def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


str2int = reduce(fn, map(char2num, "13579"))
print(str2int)


# filter
def is_odd(number):
    return number % 2 == 1


odd_list = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(odd_list)


# 利用filter将一个序列中的空字符串删除
def not_empty(s):
    return s and s.strip()


not_empty_list = list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))
print(not_empty_list)


# 用filter求素数 -- 没有怎么看懂
# 首先定义一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 然后定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 输出结果：
print("1000以内的所有素数： ")
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
# 匿名函数
sum = lambda x: x * x
result_funt = sum(5)
print(result_funt)

# 使用sorted对list进行排序
number_list = [36, 5, -12, 9, -21]
new_number_list = sorted(number_list)
print(new_number_list)
# 在sorted的基础上使用key函数实现自定义排序
# 按照绝对值大小排序：
abs_list = sorted([36, 5, -12, 9, -21], key=abs)
print(abs_list)
# 对字符串进行排序
str_list = ['bob', 'about', 'Zoo', 'Credit', ]
new_str_list = sorted(str_list)
print(new_str_list)
# 忽略字母大小写，按照字母序进行排序
new1_str_list = sorted(['bob', 'about', 'Zoo', 'Credit', ], key=str.lower)
print(new1_str_list)
# 反向排序
new2_str_list = sorted(['bob', 'about', 'Zoo', 'Credit', ], key=str.lower, reverse=True)
print(new2_str_list)

'''
对于一个求和函数，如果不需要立刻求和，而是在后面的代码中，根据需要再计算。这时就可以不返回求和的结果，而是返回求和的函数
'''


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 我们调用lazy_sum()时，返回的并不是求和结果而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)
print(type(f))
print(f())
'''
每次调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数，并且返回的两个函数是并不相同的，它们的调用结果互不影响
'''
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


# 在闭包中使用循环变量
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), '', f2(), '', f3())


# 装饰器
# 函数对象的name属性可以拿到函数的名字
def fun_a():
    return True


print(fun_a.__name__)


# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


# 借助Python的@语法，把decorator置于函数的定义处
@log
def now():
    print('2015-3-25')


# 把@log语句放到now()函数的定义出，相当于执行了语句：
# now = log(now)
now()

"""上述函数的解析： 
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(args, *kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
"""


# 完整的decorator
# 不需要参数的decorator
def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 需要参数的decorator
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(text)
            return func(*args, **kw)

        return wrapper

    return decorator


@log2("Bowenkei")
def now2():
    print("Hello World!")


now2()
print(now2.__name__)

# 偏函数
# 使用便函数创建一个新的int2()用于二进制字符串转换
int2 = functools.partial(int, base=2)
print(int2('10010'))
# 使用PIL下的Image生成一个缩略图
im = Image.open('touxiang.JPG')
print(im.format, im.size, im.mode)
'''
# 下一行用于修改图片大小
im.thumbnail((200, 100))
im.save("newtouxiang.JPG")
im.show()
'''


# 类和实例
# 创建Student类
class Student(object):
    pass


"""
括号中的object表示该类是从哪个类继承下来的。如果没有合适的继承类，就是用object类，这是所有类最终都会继承的类
创建实例是通过类名+()实现的
"""
one_Student = Student()
print(type(one_Student))
print(id(one_Student))
# id()函数用于获取对象的内存地址
# 给实例bart绑定一个name属性：
bart = one_Student
bart.name = 'Bart Simpson'
bart.age = 16
print(bart.name)
print(bart.age)
print(id(bart))


# 可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的init方法，可以在创建实例的时候，
# 就把name，score等属性绑上去
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__money = 100
        self.money = 100

    def get__money(self):
        return self.__money

    def set__monty(self, money):
        self.__money = money


class Student1(object):
    def __init__(self):
        self.name = 'bowenkei'
        self.score = 100


no1 = Student("chenqiaochu", 100)
no2 = Student1()
print("--------------------------")
print(str(no1.score) + " " + no1.name)
print(str(no2.score) + " " + no2.name)
# 注意到init方法的第一个参数永远是self，表示创建的实例本身，因此，在init方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
print(no1.money)
# 下面这行代码是尝试绕过私有变量的设定对Student中的私有变量__money进行访问
print(no1._Student__money)
print(no1.get__money())
no1.set__monty(100000)
print(no1.get__money())


# 继承和多态
# 继承
class Animal(object):
    def introduce(self):
        print("This is a animal.")

    def run(self):
        print("Animal is running.")


# 创建Cat和Dog类实现对Animal类的继承
class Dog(Animal):
    def introduce(self):
        print("This animal is a dog.")

    def run(self):
        print("The dog is running.")


class Cat(Animal):
    def introduce(self):
        print("This animal is a cat.")

    def run(self):
        print("The cat is running.")


# 创建Animal实例
one_Animal = Animal()
one_Animal.introduce()
one_Animal.run()

# 创建Cat和Dog的实例
one_Dog = Dog()
one_Dog.introduce()
one_Dog.run()

one_Cat = Cat()
one_Cat.introduce()
one_Cat.run()


def run_twice(animal):
    animal.run()
    animal.run()


class Timer(object):
    def run(self):
        print("Start...")


run_twice(Timer())

# 使用type()判断基本类型
print(type(123))
# 使用type()判断一个函数或者类
print(type(Animal()))
print(type(no1))
# 如果在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123) == type(567))
print(type(123) == int)
# 比较基本类型时可以直接写int，str等，但是如果要判断一个对象是否是函数，可以使用types模块中定义的常量
import types


def fn():
    pass


print("------------------------------------")
# 判断fn是否是一个函数
print(type(fn) == types.FunctionType)
# 判断abs
print(type(abs) == types.BuiltinFunctionType)
# 判断lambda
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
ge = (x for x in range(10))
print(next(ge))

print("------------------------------------")
# 使用isinstance()判断对象的继承关系
# 使用isinstance()判断一个变量是否是某些类型中的一个
# 判断某个变量是否是list或者tuple:
print(isinstance([1, 2, 3, 4, 5, 6], (list, tuple)))
print(isinstance((1, 2, 3, 4, 5, 6), (list, tuple)))
print(isinstance('hello', (list, tuple)))

print("------------------------------------")
# 使用dir()
# 获得一个str对象的所有属性和方法
print(dir('str'))
# __len__和len()是等价的，使用后者，它会自动去调用该对象的__len__()
print(len('abc'))
print('abc'.__len__())

print("------------------------------------")


# 使用getattr(),setattr(),hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# 测试上面新创建的对象的属性
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

print("------------------------------------")
# 使用getattr()时，可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', '404: No such a attribute'))

print("------------------------------------")
# 可以获得对象的方法
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
res = getattr(obj, 'power')
print(res())

print("------------------------------------")


# 实例属性和类属性
# 给实例绑定属性
class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 19


# 给类添加类属性
class Student1(object):
    name = 'Student'


# 上面的name就是类属性。类属性虽然归类所有，但是该类的所有实例都可以访问到
s = Student1()
print(s.name)
print(Student1.name)
s.name = "Michael"
# 因为实例属性的优先级比类属性高，所以他会屏蔽掉类的name属性
print(s.name)
# s有了实例属性之后，Student的name类属性还在且不会消失
# 在删除掉s的实例属性之后，name类属性就会显示出来
del s.name
print(s.name)

print("------------------------------------")


# 面向对象高级编程
# 使用slots
# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age


# 给实例绑定一个方法
s.set_age = types.MethodType(set_age, s)
s.set_age(20)
print(s.age)


# 但是给一个实例绑定的方法，对于另一个实例是不起作用的
# 想要给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score


Student1.set_score = types.MethodType(set_score, Student1)
s.set_score(100)
print(s.score)
s2 = Student1()
s2.set_score(10000)
print(s2.score)


# 使用slots
class Student2(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
    pass


print("------------------------------------")


# iter
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a， b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 推出循环
            raise StopIteration()
        return self.a


# Test
for n in Fib():
    print(n)

print("------------------------------------")


# getitem
def __getitem__(self, n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a


Fib.__getitem__ = types.MethodType(__getitem__, Fib)
# 现在可以按下标访问数列的任意一项了
f = Fib()
print(f[0])

print("------------------------------------")
# 让Fib实现切片
# 删除原来的__getitem__方法
del Fib.__getitem__


def __getitem__(self, n):
    if isinstance(n, int):
        a, b = 1, 1
        for x in n:
            a, b = b, a + b
        return a
    if isinstance(n, slice):
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        a, b = 1, 1
        L = []
        for x in range(stop):
            if x >= start:
                L.append(a)
            a, b = b, a + b
        return L


# 把新的__getitem__添加到Fib class中去
Fib.__getitem__ = types.MethodType(__getitem__, Fib)
# 现在可以尝试Fib的切片了
f = Fib()
print(f[0:5])
print("----------------------------")


# __getattr__()
class my_getattr(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return 99


one_getattr = my_getattr('Bowenkei')
print(one_getattr.name)
print(one_getattr.score)
# 使用__getattr__()返回函数也是可以的
del my_getattr.__getattr__


def __getattr__(self, attr):
    if attr == 'money':
        return lambda: '这是我的存款：∞'


my_getattr.__getattr__ = types.MethodType(__getattr__, my_getattr)

two_getattr = my_getattr("bowenkei")
print(two_getattr.money)
print(two_getattr.money())
# 注意，只有在没有找到属性的情况下，才调用__getattr__(),对于已经存在的属性，不会在__getattr__中查找
print(two_getattr.today)  # None
# 如上述任意调用都会返回None，因为__getattr__()的默认返回值就是None,但是如果类中没有__getattr__()
# 方法的时候，调用class中没有的熟悉则都会抛出AttributeError。要让class只响应特定的几个属性，我们就要按照约定，
# 抛出AttributeError的错误
del my_getattr.__getattr__


def __getattr__(self, attr):
    if attr == 'age':
        return lambda: 20
    raise AttributeError("\'my_getattr\'object has no attribute \'%s\'" % attr)


my_getattr.__getattr__ = types.MethodType(__getattr__, my_getattr)
three_my_getattr = my_getattr("bowenkei")
print(three_my_getattr.age())


# 由此可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况做调用
# 如果要写SDK，给每个URL对应的API都写一个方法，那太麻烦，而且API一旦改动，SDK也要改
# 利用完全动态的__getattr__(),可以写出一个链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


# Demo
print(Chain('bowenkei').status.user.timeline.list)
print(Chain('bowenkei').status)
print(Chain('bowenkei').status.user)
print(Chain('bowenkei').status.user.timeline)
print(Chain('bowenkei').status.user.timeline.list)
"""output:
bowenkei/status/user/timeline/list
bowenkei/status
bowenkei/status/user
bowenkei/status/user/timeline
bowenkei/status/user/timeline/list
"""
print("----------------------------")


# call
# 在Python中可以直接在实例本身上调用实例方法
# 任何类，只要实现一个call()方法就可以直接对实例进行调用
class Call_student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


call_s = Call_student('bowenkei')
call_s()
"""
call()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
"""
# 如何判断一个变量是对象还是函数？
# 能被调用的对象就是一个Callable对象
# 函数和带有call()的类实例都是Callable对象
# 使用callable()
print(callable(Call_student))

print("----------------------------")
# 使用枚举类
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 输出枚举成员
print(Month.Jan.value)
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# value属性是自动赋给成员的int常量，默认从1开始计数
# 从Enum中派生出自定义类
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# @unique是一个装饰器，可以帮助我们检查有没有重复值
# 访问枚举类型可以有若干种方法
print(Weekday.Mon)
print(Weekday['Sat'])
print(Weekday(1))
# 即既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量

# 断言(assert)
"""
def foo(s):
    n = int(s)
    assert n != 0, '0 is zero!'
    return 10 / n

def main():
    foo('0')

main()
"""
# assert的意思是，表达式n!=0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。如果断言失败，
# assert语句本身就会抛出AssertionError
# 启动python解释器时可以用 -0 参数(python3 -0 python_file_name)来关闭assert，关闭后，所有的assert语句可以当成pass
'''
# logging
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info("n = %d" % n)
print(10 / n)
'''
# info是通告，信息的意思
# logging的好处就是，它允许你使用不同的参数来区分记录信息的级别，可选的参数有debug, info, waring, error。
# 当我们选定其中info的时候哦，logging.debug就不起作用了，这样就可以输出不同级别的信息，也不用删除。
# 使用logging的另外一个好处是，通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件




