#这是计算三角形面积的实例：
import cmath
a = float(input("Please give me the a-length of sanjiaoxing:"))
b = float(input("Please give me the b-length of sanjiaoxing:"))
c = float(input("Please give me the c-length of sanjiaoxing:"))
half_length = (a+b+c)/2
S = half_length*(half_length-a)*(half_length-b)*(half_length-c)
S_ = cmath.sqrt(S)
print("The S of your sanjiaoxing is :{}".format(S_))
