class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num

        return result


nums = [4, 1, 2, 1, 2]

sol = Solution()

print(sol.singleNumber(nums))
