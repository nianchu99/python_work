#判断闰年
a = int(input("Please give a year:"))
if a%400==0:
    print("这是一个闰年")
elif a%4==0:
    print("这是一个闰年")

else:
    print("抱歉，这不是一个闰年。")