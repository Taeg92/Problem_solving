from itertools import combinations

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}

        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], i]
            nums_dict[num] = i

        
nums = [3,3] 
target = 6
# Output: [0,1]

sol = Solution()
print(sol.twoSum(nums, target))
