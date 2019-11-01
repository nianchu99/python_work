#下面这个实例用于判断一个用户输入的数字是整数负数还是零
a = int(input("Enter a number:"))
if a == 0:
    print("The number is 0")
elif a >= 0:
    print("这个数字是正数。")

else:
    print("这是一个负数，抱歉！")
