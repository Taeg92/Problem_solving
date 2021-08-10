class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        answer = [num for num in nums if num != val]
        for i in range(len(answer)):
            nums[i] = answer[i]

        nums = nums[:len(answer)]

        return len(nums)


nums = [3, 2, 2, 3]
val = 3
# Output : 2
sol = Solution()
print(sol.removeElement(nums, val))
