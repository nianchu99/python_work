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
    str2dt_new = str2dt.replace(tzinfo=set_timezone)  # 使用replace之后必须复制给另外一个变量，否则tzinfo无法修改

    return str2dt_new.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('Pass')

# collections
# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p.x)
print(p.y)

"""
namedtuple是一个函数，用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
下面验证Point的类型：
"""
print(isinstance(p, Point))
print(isinstance(Point, tuple))
print(isinstance(p, tuple))

# 下面使用namedtuple定义一个圆
Circle = namedtuple('Circle', ['x', 'y', 'radius'])
# 创建一个圆形
circle = Circle(0, 0, 5)
print("The center of the circle is (%d, %d), and its radius is %s " % (circle.x, circle.y, circle.radius))

# deque
"""
deque除了实现list的append()和pop()外，还支持appendleft()和popleft(),这样就可以非常高效地往头部添加或删除元素
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
"""
from collections import deque

q = deque(['a', 'b', 'c', 5])
print(q)
q.append('d')
print(q)
q.appendleft("The left one")
print(q)
q.popleft()
print(q)

# defaultdict
'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
默认值是调用函数返回的，函数在创建defaultdict对象时传入
除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
'''
from collections import defaultdict

dd = defaultdict(lambda: 'The default value')
dd['key1'] = ' The value of key1'
print(dd['key1'])  # The value of key1
print(dd['key2'])  # The default value

# OrderedDict
'''
dict是无序的，如果要保持Key的顺序，可以使用OrderedDict;
OrderedDict的Key会按照插入的顺序排列，不是Key本身排序；
'''
from collections import OrderedDict
d = dict(a=1, c = 3, b = 2)  # {'a': 1, 'b': 2, 'c': 3} ——--- Python3.6以后dict也是有序的了。
print(d)
# 实现Orderedict
d1 = OrderedDict(d)
print(d1)
# OrderedDict可以实现一个FIFO(先进先出)的dict，当容量超出限制时，先删除最早添加的Key：
# 下面这个实现没有怎么看懂
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.__capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self.__capacity:
            last = self.popitem(last=False)
            print('remove', last)

        if containsKey:
            del self[key]
            print('set', (key, value))

        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)

# Counter： 一个简单的计数器
# 使用Counter统一字符串中字符出现的次数
# Counter就是一个dict
from collections import Counter
c = Counter()
s = 'today is a good day, it\'s a good time to learn something'
for ch in s:
    c[ch] = c[ch] + 1

print(c)

# base64
# 解编码
import base64
# 编码
bs1 = base64.b64encode(b'binary string')
print(bs1)
# 解码
bs2 = base64.b64decode(bs1)
print(bs2)

# 使用url-safe的base64编码
'''
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
'''
bs3 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bs3)  # b'abcd++//' ---- 字符+和/没有改变
bs4 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bs4)  # 字符+和/分别变成了-和_


# 小节练习
def safe_base64_decode(s):
    if len(s) != 4:
        s = s + bytes('=', encoding='utf-8') * (4 - len(s) % 4)

    if not isinstance(s, bytes):
        s = bytes(s, encoding='utf-8')

    # 解码
    return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

# struct
# struct的pack函数把任意数据类型变成bytes
import struct
s = struct.pack('>I', 10240099)
print(s)  # b'\x00\x9c@c'
# 上面>表示： 字节顺序是big-endian，也就是网络序；I表示4字节无符号整数
# 后面的参数个数要和处理指令一致
# unpack把bytes变成相应的数据类型
four_bytes_int, two_bytes_int = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(four_bytes_int)  # 4042322160
print(two_bytes_int)  # 32896
# H表示2字节无符号整数

# 小节练习
# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
import struct
# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

def bmpinfo(s):
    if not isinstance(s, bytes):
        s = bytes(s, encoding='utf-8')
    if s[0:2] == (b'BM' or b'BA'):
        result = struct.unpack('<ccIIIIIIHH', s)
        photo_size = result[-4:-2]
        print("此位图的大小是：%d x %d" % (photo_size[0], photo_size[1]))
        print("此位图的颜色数是：%d" % result[len(result) - 1])

    else:
        print("抱歉， 这不是一个位图。")

bmpinfo(s)
s1 = 'fdsfsdfsdfdsf'
bmpinfo(s1)

"""
output:
b'BM'
此位图的大小是：640 x 360
此位图的颜色数是：24
b'fd'
抱歉， 这不是一个位图。
"""
# hashlib
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
'''
MD5是常见的摘要算法，速度很快，生成结果是固定的128bit字节，通常用一个32位的16进制字符串表示。
'''

"""
另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
"""
sh1 = hashlib.sha1()
sh1.update('how to use sha1 in '.encode('utf-8'))
sh1.update('python hashlib?'.encode('utf-8'))
print(sh1.hexdigest())
""""
SHA1的结果是160bit字节，通常用一个40位的16进制字符串表示
"""

import hashlib


# 1 - 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    s = str(password)
    one_md5 = hashlib.md5()
    one_md5.update(s.encode('utf-8'))

    return one_md5.hexdigest()


print(calc_md5("todayisaniceday."))

# 2 - 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    s = str(password)
    one_md5 = hashlib.md5()
    one_md5.update(s.encode('utf-8'))
    return one_md5.hexdigest() == db[str(user)]


print(login('michael', 123456))
print(login('bob', '888888'))
print(login('alice', password=123456))



import hashlib

# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
salt_value = 'the-Salt'
db = {}
def register(username, password):
    db[username] = get_md5(password + username + salt_value)



def get_md5(password):
    s = str(password)
    one_md5 = hashlib.md5()
    one_md5.update(s.encode('utf-8'))
    return one_md5.hexdigest()



# 测试
register('bob', 'hello world')
print(db)  # {'bob': '7fa0c1935fed7e7730be403321f3b04c'}
register('bowenkei', 'today is a good day')
print(db)

# 根据修改后的MD5算法实现用户登录的验证：
def login(user, password):
    return db[str(user)] == get_md5(str(password) + str(user) + salt_value)


# Test
print(login('bob', 'hello world'))
print(login('bowenkei', 'today is a good day'))
print(login('bowenkei', 123456))

# itertools
# count()会创建一个无限迭代器。
import itertools
naturals = itertools.count(100) # count()括号里面的数字指定了从哪一个数字开始数
print(naturals.__next__())
print(naturals.__next__())

# cycle() —— 会把传入的一个序列无限重复下去
abc = itertools.cycle(['a', 'b', 'c'])
for i in range(3 * 2):  # 这里指定了次数，避免出现死循环
    print(abc.__next__())

# repeat()负责将一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)  # 迭代了三次

# 无限序列虽然可以无限迭代下去，但是通常会通过takenwhile()等函数根据条件判断来截取一个有限的序列：
naturals = itertools.count(1)
ns = itertools.takewhile(lambda x:x <= 10, naturals)
print(ns)
print(list(ns))

# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
new_iter = itertools.chain('ABC', 'XYZ')
print(list(new_iter))  # ['A', 'B', 'C', 'X', 'Y', 'Z']

# proupby()
# groupby把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBBBBDDDDCCCCAAA'):
    print(key, list(group))

# 向groupby中传入一个函数可以实现忽略大小写：
for key, group in itertools.groupby('AAABBBBbcdaabccBBDDDDCCCCAAA', lambda c: c.upper()):
    print(key, list(group))

from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print("sax:start_element: %s, attrs: %s" % (name, str(attrs)))

    def end_element(self, name):
        print("sax:end_element: %s" % name)

    def char_data(self, text):
        print("sax:char_data: %s " % text)



xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)



