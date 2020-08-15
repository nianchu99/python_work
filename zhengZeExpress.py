import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4242. ')

'''search 方法接受传入的字符串，如果字符串中没有找到符合该正则表达式模式，search返回None，如果找到了该模式，search返回一个Match对象'''
'''Match对象有一个group方法，它返回被查字符串中实际匹配的文本'''
print('Phone number found : ' + mo.group())

"""Python 正则表达式使用步骤：
1 用import re导入正则表达式模块
2 用re.compile()函数创建一个Regex对象(注意使用原始字符串)
3 向Regex对象的search方法传入想查找的字符串。它返回一个Match对象
4 调用Match对象的group方法，返回实际匹配文本的字符串"""

# 匹配更多模式

'''将区号从号码中分离出来'''
phoneNumberRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumberRegex1.search("My phone number is 232-243-7642")
print("My phone's 区号 is :" + mo1.group(1))  # 输出区号(1组)
print("My phone's not区号 is :" + mo1.group(2))  # 输出区号(2组) 

# 一次获取所有分组 group()方法----将返回包含多个值的数组
print("There are: ")
print(mo1.groups())
# 在正则表达式中使用括号需要用"/"转义符
myNumbers = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
results = myNumbers.search("我的电话号码是: (123)-456-7980")
print(results.group())

# 用管道匹配多个字符 ： '|'
"""字符|称为“管道”。希望匹配许多表达式中的一个时，就可以使用它。例如，正则表达式r'Batman|TinaFey'将匹配'Batman'或'TinaFey'。"""
"""如果Batman 和 Tina Fey都出现在被查找的字符串中，第一次出现的匹配文字，将作为Match对象返回"""
testZhongWen = re.compile(r'雷博闻')
testZhongWen1 = re.compile(r'陈翘楚|雷博闻')

results = testZhongWen.search("陈翘楚喜欢雷博闻")
print(results.group())
results1 = testZhongWen1.search("陈翘楚和雷博闻他们相亲相爱")
print(results1.group())
"""注意：当匹配结果只有一个，却非要用groups去返回对象时，返回值是一对()"""
"""有多个匹配时，使用findall()方法可以找到多个匹配的地方"""  # 根据输出结果来看，findall将返回所有匹配对象的一个字符串列表
results2 = testZhongWen1.findall("陈翘楚和雷博闻他们相亲相爱")
print(results2)

## 用管道来匹配多个模式中的一个，作为正则表达式的一部分
chenYi = re.compile(r'Chen(QiaoChu|Jing|Dream)')
chenYiResults = chenYi.search("There are two beautiful girls, they are ChenQiaoChu and ChenJing")
chenYiResults1 = chenYi.findall('There are two beautiful girls, they are ChenQiaoChu and ChenJing')  # 此时用findall的返回值不包括前面的共有部分
print(chenYiResults.group())
print(chenYiResults1)

# 用问号实现可选匹配
wenHao = re.compile(r"I (don't)?love study")  # 这里？表示前面的don't是可选的，但是好像？后面不能有空格。
wenHaoRequest = wenHao.search('I love study English')
wenHaoRequest1 = wenHao.search("I don'tlove study ")
print(wenHaoRequest.group())
print(wenHaoRequest1.group())
'''你可以认为?是在说，“匹配这个问号之前的分组零次或一次”。'''

# 用星号实现零次或者多次
## 匹配一个wo
xingHao = re.compile(r"Good(wo)*man")
xingHaoResult = xingHao.search('She is a Goodwoman')
## 匹配两个wo
xingHaoResult1 = xingHao.search('She is  a Goodwowoman ')
print(xingHaoResult.group())
print(xingHaoResult1.group())
## 用加号匹配一次或多次，注意，与星号不同，加号要求至少出现一次
jiaHao = re.compile(r'(winner)+')
jiaHaoResult = jiaHao.search('winnerwinner')
print(jiaHaoResult.group())
## 若一次都没有则在调用search时就会返回None值
jiaHaoResult1 = jiaHao.search('fdsagsdag')
print(jiaHaoResult1)
# 用花括号匹配特定次数
huaKuoHao = re.compile(r'(Today){2}')
##  此时两次是能够正确匹配的
huaKuoHaoResult = huaKuoHao.search('TodayToday')
print(huaKuoHaoResult.group())
##  此时不能匹配两次以外的其他次数了
print(huaKuoHao.search('Today'))
print(huaKuoHao.search('(Today)(Today)(Today)(Today)')) ## 此时匹配会返回None(注意加上())
## {3,}匹配大于等于3次，{,5}返回小于等于5次

# 贪心和非贪心匹配
# Python正则表达式是贪心的，意思是说：如果正则模式为(Ha){3,5},给定的待查字符串为'HaHaHaHaHa'；这种情况下为什么不匹配'HaHaHa' 或者'HaHaHaHa',而只是匹配5个'Ha'呢。这就是贪心匹配
# 要想让Python实现非贪心匹配，需要在花括号后面添加？号
notTanxin = re.compile(r'(ha){3,5}?')
notTanxinResult = notTanxin.search('hahahahaha')
print(notTanxinResult.group()) # hahaha

# findall()方法 —-返回由所有匹配对象组成的字符串列表
findallTest = re.compile(r'\d\d\d-')
findallTestResult = findallTest.findall('123-fad,'
										'345-hgd')
print(findallTestResult)

# findall()方法总结
'''1．如果调用在一个没有分组的正则表达式上，例如：\d\d\d\d\d\d\d\d\d\d，方法findall()将返回一个匹配字符串的列表，例如['4155559999','2125550000']。

2．如果调用在一个有分组的正则表达式上，例如(\d\d\d)(\d\d\d)(\d\d\d\d)，方法findall()将返回一个字符串的元组的列表（每个分组对应一个字符串），例如[('415','555','1122'),('212','555','0000')]。
'''
# 字符分类
# \d是正则表达式(0|1|2|3|4|5|6|7|8|9)的缩写。
#
# [美] Al Sweigart  斯维加特. Python编程快速上手 让繁琐工作自动化 (Kindle 位置 3069-3070). Kindle 版本.
# \d: 0-9的任何数字
# \D:除0到9的数字以外的任何字符
# \w:任何字母、数字或下划线字符(可以认为是匹配"单词"字符) \W: 除字母、数字、下划线意外的任何字符 \s：空格、制表符或换行符(可以认为是匹配"空白"字符) \S：除空格、制表符和换行符以外的任何字符

# 建立自己的字符分类
"""
你可以用方括号定义自己的字符分类。例如，字符分类[aeiouAEIOU]将匹配所有元音字符，不论大小写。

也可以使用短横表示字母或数字的范围。例如，字符分类[azAZ09]将匹配所有小写字母、大写字母和数字

 """
# 非字符类： 痛过在字符分类的左方括号上加上一个插入字符(^),就可以得到"非字符类"。非字符类将匹配不在这个字符类中的所有字符
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY EOOD.'))

# 插入字符和美元字符
# ^ + string : 表明待查找字符串必须以string结尾
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.findall('Hello  world'))  #   ['Hello']
print(beginsWithHello.findall('He said hello'))  #  []
# 将$用在结尾处表明只匹配以特定字符串结尾的字符
endsWithDigit = re.compile(r'\w+\d+$')
print(endsWithDigit.findall('fetgg34324'))
print(endsWithDigit.findall('343fdsfs'))

# 通配字符：.
# 它表明匹配除了换行之外的所有字符
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
# ['cat', 'hat', 'sat', 'lat', 'mat']
# Notice: 句点字符只匹配一个字符，这就是为什么flat只匹配lat。要匹配真正的句点.需要使用转义符
atRegex1 = re.compile(r'(\S){1,}at$')
print(atRegex1.findall('flat hat cat hat hhhhat'))