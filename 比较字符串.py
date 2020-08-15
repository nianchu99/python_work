class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        a = len(A)
        b = len(B)
        geshu = 0
        tiaochu = 0
        i = 0
        j = 0
        if a >= b:
            while j < b:
                if i < a:
                    if A[i] == B[j]:
                        geshu = geshu + 1
                        i = i + 1
                        j = j + 1
                        tiaochu = tiaochu + 1
                    else:
                        i = i + 1

        if geshu == b:
            return True
        else:
            return False



so  = Solution()
print(so.compareStrings("ABCDE","DB"))