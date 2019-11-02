#九九乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print("{}*{}={}\t".format(b,a,b*a),end = '')
    print()