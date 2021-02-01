class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        check = [0] * len(nums)
        element = []

        def dfs(level):
            if level == len(nums):
                result.append(element[:])
                return
            else:
                for i in range(len(nums)):
                    if not check[i]:
                        check[i] = 1
                        element.append(nums[i])
                        dfs(level + 1)
                        element.pop()
                        check[i] = 0

        dfs(0)

        return result


nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

sol = Solution()

print(sol.permute(nums))
