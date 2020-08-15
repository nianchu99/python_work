class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        geshu=0
        a = len(source)
        b = len(target)
        if source =="" and target =="":
            return 0
        elif source !="" and target =="":
            return 0
        elif target not in source:
            return -1
        else:
            for i in range(a):
                if target[0] == source[i]:
                    for j in range(b):
                        if (i+j) < a:
                            if source[i+j] == target[j]:
                                geshu = geshu + 1

                        if geshu == b:
                             return i

so = Solution()
print(so.strStr("tartarget","target"))