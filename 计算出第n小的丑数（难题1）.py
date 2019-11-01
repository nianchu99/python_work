#用于设计一个算法，找出只含素因子2，3，5 的第 n 小的数。
#符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
from heapq import heappop, heappush
class Solution:     #heappop heappush 分别是弹出根节点和插入数据到堆中 操作
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        result_set = [1]                      #初始结果集
        factor = [2,3,5]                      #3个素因子
        if n == 1:                            #如果n=1 直接返回结果 1
            return 1
        for i in range(n):
            result = heappop(result_set)      #取出根节点
            for fac in factor:                #生成三个丑数
                tem = fac * result
                if tem not in result_set:     #若结果集中不存在该数就加入结果集
                    heappush(result_set, tem)
        return result

so = Solution()
print(so.nthUglyNumber(9))

