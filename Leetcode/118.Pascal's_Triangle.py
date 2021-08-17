class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(res[i-1][j-1]+res[i-1][j])
            temp.append(1)
            res.append(temp)
        return res


numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
sol = Solution()

print(sol.generate(numRows))
