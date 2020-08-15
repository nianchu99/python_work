#输出指定范围内的素数（这里注意看代码中关于for和else连用的用法！）
first = int(input("输入区间最小值："))
last = int(input("输入区间最大值"))
c = []
for a in range(first,last+1):
    if a > 1:
        for b in range(2,a):
            if (a%b)==0:
                break
        else:
            c.append(a)




print(c)