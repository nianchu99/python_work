#合并排序数组
"""
a=[1,3,5,7,9,10]
b=[2,4,6,8]
c=a+b
print(c)
n=len(c)
for i in range(n):
    for j in range(n-1):
        if c[j]>c[j+1]:
            ex=c[j+1]
            c[j+1]=c[j]
            c[j]=ex

print(c)
#7.二叉树还没有学
#8.原地旋转字符串//不知道偏移量是什么意思暂时没做
z=str(input())
m=len(z)
n=int(input())
"""
""""#9.Fizz Buzz问题
num=int(input("give me a number!"))
if num % 3 == 0 and num % 5 == 0:
    print("fizz buzz")
elif num % 5==0:
    print("buzz")
elif num % 3 ==0:
    print("fizz")
elif num % 3!=0 and  num %5!=0:
    print(num)
"""

""""#第k大元素
class Solution:
    

    def kthLargestElement(self, n, nums):
        m = len(nums)
        for i in range(m):
            for j in range(0,m-i-1):
                if nums[j] < nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]

        print(nums[n-1])

nums=[1,4,6,3,19]
so = Solution()
so.kthLargestElement(1,nums)
"""
a = [1,2,3,4]
for i in range(len(a)):
    print(i)