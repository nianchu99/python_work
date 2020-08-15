import itertools
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        pailie = list(itertools.permutations(nums))  # 要list一下，不然它只是一个对象

        return pailie



so = Solution()
print(so.permute([1,2,3]))
