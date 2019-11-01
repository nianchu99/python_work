#判断一个大于零的数是奇数还是偶数
number = int(input("Give me a number,then i will tell you what type it is:"))
if number<0:
    print("Sorry,it is not that we want!")
elif number%2==0:
    print("它是一个偶数。")

else:
    print("它是一个奇数，谢谢。")
