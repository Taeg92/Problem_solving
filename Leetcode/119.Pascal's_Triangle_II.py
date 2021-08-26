class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
            res.append(1)
        return res


rowIndex = 3
# Output: [1, 3, 3, 1]

sol = Solution()
print(sol.getRow(rowIndex))
