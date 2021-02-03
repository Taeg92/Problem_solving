class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        def dfs(total, s, elements):
            if total > target:
                return
            if total == target:
                result.append(elements[:])
                return

            for i in range(s, len(candidates)):
                elements.append(candidates[i])
                dfs(total + candidates[i], i, elements)
                elements.pop()

        dfs(0, 0, [])

        return result


candidates = [2, 3, 6, 7]
target = 7
# Output: [[2, 2, 3], [7]]


sol = Solution()

print(sol.combinationSum(candidates, target))
