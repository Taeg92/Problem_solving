class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(index, path):
            if path not in res:
                res.append(path)

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]])

        nums.sort()
        res = []
        dfs(0, [])
        return res


nums = [1, 2, 2]

sol = Solution()

print(sol.subsetsWithDup(nums))
