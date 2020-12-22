import sys


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            answer = max(answer, current_sum)

        return answer


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6

sol = Solution()

print(sol.maxSubArray(nums))
