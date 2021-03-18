class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 1

        nums.sort()

        for num in nums:
            if num == result:
                result += 1

        return result


nums = [0, 2, 2, 1, 1]
# Output: 1

sol = Solution()

print(sol.firstMissingPositive(nums))
