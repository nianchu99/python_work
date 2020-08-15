class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        A.extend(B)
        n = len(A)
        print(A)
        for i in range(n):
            for j in range(0,n-i-1):
                if A[j] > A[j+1]:
                    A[j],A[j+1] = A[j+1],A[j]

        return A
a=[7]
b=[5,7]
so = Solution()
print(so.mergeSortedArray(a,b))