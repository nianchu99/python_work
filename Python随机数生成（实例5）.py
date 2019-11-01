#使用random模块来生成随机数
import random
#1.从序列的元素中取出一个数字来
numbers = [1,2,3,4,5,6,7,8,9,10]
a = random.choice(numbers)
print(a)
#2.从range范围内取值
print(random.choice(range(1,100)))
#3.从字符中抓取
print(random.choice("I love you very much!"))
#4.从多个字符串的列表中随机取
list = ["China","America","UN","Shanghai","Chongqing"]
print(random.choice(list))
#5.使用randrang方法
print(random.randrange(1,100,2))#括号中的三个参数，第一个是开始值，随机抽取时包括在内，
# 第二个是结束值，随机抽取时不包括在内，最后一个是步长。
#6.取出随机的一个整型数
print(random.randint(1,522))
#7.随机取出0-1之间的数字
print(random.random())
#8.将序列的元素重新排序
list = [5,2,0,1,3,1,4]
random.shuffle(list)
b = list
print(b)
#输出结果分别为：10
#77

#China
#71
#446
#0.8079504733594368
#[5, 1, 0, 2, 4, 3, 1]
