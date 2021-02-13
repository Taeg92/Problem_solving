class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]


nums = [3, 2, 3]
# Output: 3

sol = Solution()
print(sol.majorityElement(nums))
