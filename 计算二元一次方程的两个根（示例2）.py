import cmath
a,b = int(input("Please give me the value of a:")),int(input("Please give me the value "
                                                    "of b:"))
c = int(input("Please give me the value of c:"))
print("This is fuction that you want to solve:{}x*x+({})x+({})=0\n".format(a,b,c))
d = b*b-4*a*c
m = cmath.sqrt(d)
x1 = (-b+m)/2*a
x2 = (-b-m)/2*a
print("These are your answers:{},{}\n".format(x1,x2))
#输出结果为：
#Please give me the value of a:1
#Please give me the value of b:-2
#Please give me the value of c:-15
#This is fuction that you want to solve:1x*x+(-2)x+(-15)=0

#These are your answers:(5+0j),(-3+0j)

