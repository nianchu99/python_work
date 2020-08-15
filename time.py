#Pyton实现简单的计算器，满足加减乘除
#定义函数
def add(x,y):
	return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def devide(x,y):
  return x/y
print("1->加法")                      #规定选择
print("2->减法")
print("3->乘法")
print("4->除法")
yours=int(input("请选择运算类型："))#获取用户选择
a=int(input("first number"))     #获取要运算的数字
b=int(input("second number"))
if yours==1:                    #判断用户需要的运算类型并输出结果
     print("{}+{}={}".format(a,b,add(a,b)))
elif yours==2:
    print('{}-{}={}'.format(a,b,subtract(a,b)))
elif yours==3:
    print('{}-{}={}'.format(a, b, multiply(a, b)))
else:
    print('{}-{}={}'.format(a, b,devide(a, b)))

'''运行结果为：
1->加法
2->减法
3->乘法
4->除法
请选择运算类型：4
first number1000
second number10
1000-10=100.0
'''
