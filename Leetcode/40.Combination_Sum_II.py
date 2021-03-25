class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(index, path, target):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, path + [candidates[i]], target - candidates[i])

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


candidates = [10, 1, 2, 7, 6, 1, 5]

target = 8

sol = Solution()

print(sol.combinationSum2(candidates, target))
