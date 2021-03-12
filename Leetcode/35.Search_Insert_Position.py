class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def get_idx(nums):
            idx = -1
            for i in range(len(nums)):
                if nums[i] == target:
                    idx = i

            return idx

        def get_insert_pos(nums, target):

            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return i + 1

        index = get_idx(nums)

        if index == -1:
            return get_insert_pos(nums, target)
        return index


sol = Solution()

nums = [1, 3, 5, 6]
target = 2

print(sol.searchInsert(nums, target))
