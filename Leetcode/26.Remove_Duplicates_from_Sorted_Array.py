class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0

        for i in range(1, len(nums)):
            if nums[cnt] != nums[i]:
                cnt += 1
                nums[cnt] = nums[i]

        return cnt + 1


nums = [1, 1, 2]
# Output : 2
sol = Solution()
print(sol.removeDuplicates(nums))
