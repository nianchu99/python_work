from functools import reduce
import functools

"""练习
def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# 我的解法： 
def str2float(s):
    devide = 1
    lenOfSmallNumber = 0
    index_of_point = 0
    for i in range(len(s)):
        if s[i] == '.':
            lenOfSmallNumber = len(s) - i - 1
            index_of_point = i
    s = s[:index_of_point] + s[index_of_point + 1 :]
    print(s)
    def change(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def fn(x, y):
            return x * 10 + y
    result = reduce(fn, map(change, s))

    for i in range(lenOfSmallNumber):
        devide = devide * 10

    return result / devide



print('str2float(\'123.456\') =', str2float('123.456'))


# 大神解法：
def str2float1(s):
    def fn(x, y):
        return x * 10 + y

    n = s.index('.')
    s1 = list(map(int, [x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n + 1:]]))
    return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)


print('str2float(\'123.456\')=', str2float1('125435433.456643565435546'))
# 自己对上述解法的理解(其实很简单，一看就懂了，难得写了）
# 但是有一点我是需要写出来的，那就是上面这个更厉害的方法在给定数字太大的情况下是同样会出现误差的

# 利用filter输出1000以内的回数
def is_palindrome(n):
    str_number = str(n)
    for i in range(len(str_number)):
        if str_number[i] == str_number[len(str_number) - 1 - i]:
            continue
        else:
            return False
    return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))
#
# 请用sorted()对上述列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):

    return t[0]

L2 = sorted(L, key=by_name)
print(L2)
# 请用sorted()对上述列表分别按成绩高低排序
def by_score(t):
    return t[1]

L3 = sorted(L, key=by_score)
print(L3)
"""
"""
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin call")
        c = func(*args, **kw)
        print("end call")
        return c
    return wrapper

# @log 的意思是 now = log(now)
@log
def now():
    print("execute success!")


now()
"""

"""
# 能否写出一个@log的decorator，它支持参数也支持没有参数
def log(text = ''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if text != '':
                print(text)
            func()
            print("call end")
            return func
        return wrapper
    return decorator


@log('hello world')
def my_func():
    print("success")


my_func()
"""

"""
# 写出这样的链式调用：Chain().user('michael').repos以实现类似GitHub这样的API:GET /user/:user/repos
class Chain(object):
    def __init__(self, path='GET /users'):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def user(self, user):
        return Chain('%s/:%s' % (self._path, user))

    def __str__(self):
        return self._path

    __repr__ = __str__
# Demo
print(Chain().user('michael').repos)
# success
"""


"""
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
"""
# 有点意思
'''
import os
def search_file(dir,sname):
    if sname in os.path.split(dir)[1]: #检验文件名里是否包含sname
        print(os.path.relpath(dir)) #打印相对路径，相对指相对于当前路径
    if os.path.isfile(dir):   # 如果传入的dir直接是一个文件目录 他就没有子目录，就不用再遍历它的子目录了
        return

    for dire in os.listdir(dir): # 遍历子目录  这里的dire为当前文件名
        search_file(os.path.join(dir,dire),sname) #jion一下就变成了当前文件的绝对路径
                                           # 对每个子目录路劲执行同样的操作



search_file('.', ' ')
'''

'''
1.1 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email
1.2 版本二可以提取出带名字的Email地址
'''
'''
import re
# Version 1
# someone@gmail.com
# bill.gates@microsoft.com
email_1 = re.compile(r'^[\w\.]+@[\w]+\.com$')
print(email_1.match('someone@gmail.com'))
print(email_1.match('bill.gates@microsoft.com'))
print(email_1.match('nianchucqc@gmail.com'))

# Version 2
# <Tom Paris> tom@voyager.org

email_2 = re.compile(r'^(<)([\w\.\s]+)(>)(\s[\w\.\s]+@[\w\.\s]+)$')
print(email_2.match('<Tom Paris> tom@voyager.org').group(2))
'''

"""
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
"""
# answer
import re
from datetime import timezone, datetime, timedelta
def to_timestamp(dt_str, tz_str):
    dt_com = re.compile(r'UTC([+|-][\d]{1,2}):00')
    tz = dt_com.match(tz_str).group(1)
    int_tz = int(tz)
    set_timezone = timezone(timedelta(hours=int_tz))
    str2dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    str2dt_new = str2dt.replace(tzinfo=set_timezone) # 使用replace之后必须复制给另外一个变量，否则tzinfo无法修改

    return str2dt_new.timestamp()




# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('Pass')
