#这个脚本用来进行简单的交换变量
a = int(input("Give me a number:"))
b = int(input("Please give me a number again:"))
c = a
a = b
b = c
print("These numbers are acted by changing.")
print("a has changed to {},b has changed to {}".format(a,b))
#输出结果是：
#Give me a number:520
#Please give me a number again:999
#These numbers are acted by changing.
#a has changed to 999,b has changed to 520
