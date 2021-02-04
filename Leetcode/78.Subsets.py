class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(s, elements):

            result.append(elements)

            for i in range(s, len(nums)):
                dfs(i + 1, elements + [nums[i]])

        dfs(0, [])
        return result


nums = [1, 2, 3]

sol = Solution()

print(sol.subsets(nums))
