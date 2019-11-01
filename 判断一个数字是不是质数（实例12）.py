#判断一个数是不是质数
number = int(input("give me a number :"))
if number  > 1:
    for i in range(2,number):
        if number%i==0:
            print("这不是一个质数")
            print(i,"*",number//i,"等于",number)
            break
        else:
            print("这是一个质数。")
