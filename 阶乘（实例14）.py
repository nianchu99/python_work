#阶乘实例
a = int(input("Give me a number :"))
i = 1
for c in range(1,a+1):
    i = i * c

print(a,"的阶乘是：{}".format(i))