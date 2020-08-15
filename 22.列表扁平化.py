class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        a = []
        for i in range(len(nestedList)):
            if type(nestedList[i]) == list:
                for j in range(len(nestedList)):
                    if type(nestedList[j]) != list:
                        a.append(nestedList[j])
                    else:
                        for k in range(len(nestedList[j])):
                            a.append((nestedList[j])[k])
                return Solution.flatten(self,a)

        return nestedList



nums = [4,[3,[2,[1]]]]
so = Solution()
print(so.flatten(nums))