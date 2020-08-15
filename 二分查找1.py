class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if  nums[mid] == target:
                    while(mid >= 0):
                        if nums[mid] != target:
                            break

                        mid = mid - 1
                    if mid <= -1:
                        return 0
                    return mid + 1
                elif  target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1

            return -1



nums = [4,5,9,12,13,14,15,15,18]
so = Solution()
print(so.binarySearch(nums,9))