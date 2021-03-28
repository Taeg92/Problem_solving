class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        avail_idx = 0

        for idx in range(len(nums)):

            if idx != 0 and avail_idx < idx:
                return False

            max_idx = idx + nums[idx]

            if avail_idx < max_idx:
                avail_idx = max_idx

            if len(nums) - 1 <= max_idx:
                return True

        return False


nums = [2, 3, 1, 1, 4]

sol = Solution()

print(sol.canJump(nums))
