class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()


nums = [2, 0, 2, 1, 1, 0]
# Output: [0,0,1,1,2,2]

sol = Solution()

print(sol.sortColors(nums))
