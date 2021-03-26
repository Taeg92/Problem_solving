from itertools import permutations


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permu_list = list(set(permutations(nums, len(nums))))

        for i in range(len(permu_list)):
            permu_list[i] = list(permu_list[i])

        return permu_list


nums = [1, 1, 2]
# Output: [[1,1,2], [1, 2, 1], [2, 1, 1]]

sol = Solution()

print(sol.permuteUnique(nums))
