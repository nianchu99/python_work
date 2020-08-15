class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

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
