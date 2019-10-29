#语法：str.join(sequence)
#参数：sequence:要连接的元素序列
#   str:指定的字符
#返回值：返回通过指定字符连接序列中元素生成的新字符
#示例：
a = [1,2,3,4,5,6,7,8]
d = list(map(str,a))
b = "--"
c = b.join(d)
print(c)
#输出结果为：1--2--3--4--5--6--7--8