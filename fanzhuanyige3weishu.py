class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        g = number%10
        s = (int(number/10))%10
        b = int(number/100)
        print( g * 100 + s * 10 + b)

so = Solution()
print(so.reverseInteger(121))
