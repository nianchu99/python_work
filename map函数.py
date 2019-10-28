#描述：
#map() 会根据提供的函数对指定序列做映射。
#第一个参数 function 以参数序列中的每一个元素调用 functio
#语法：map(function, iterable, ...)
#示例：
def biaodashi (m,n):
    y = m*n+m/n
    return y
a = list((map(biaodashi,[1,2,3],[3,2,1])))
print(a)
#结果输出为：[3.3333333333333335, 5.0, 6.0]
#注意：map()的输出结果是迭代式，需要使用list才能转换为列表
