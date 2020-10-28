class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        nums.sort()
        for i in range(len(nums) // 2):
            total += nums[2 * i]
        return total


nums = [6, 2, 6, 5, 1, 2]
# Output: 4

sol = Solution()

print(sol.arrayPairSum(nums))
