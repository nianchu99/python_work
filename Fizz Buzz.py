class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        a = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                a.append("fizz buzz")
            elif i % 3 == 0:
                a.append("fizz")
            elif i % 5 == 0 :
                a.append("buzz")
            else:
                a.append("{}".format(i))


        return a

so = Solution()
print(so.fizzBuzz(15))