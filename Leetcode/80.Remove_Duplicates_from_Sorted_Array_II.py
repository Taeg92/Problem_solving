class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0

        for num in nums:
            if idx < 2 or num != nums[idx-2]:
                nums[idx] = num
                idx = idx + 1

        return idx


nums = [1, 1, 1, 2, 2, 3]
sol = Solution()

print(sol.removeDuplicates(nums))
