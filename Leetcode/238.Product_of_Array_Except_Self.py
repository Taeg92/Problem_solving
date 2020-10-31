class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        left = [0]*len(nums)
        right = [0]*len(nums)

        prod = 1
        for i in range(len(nums)):
            left[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(len(nums)-1, -1, -1):
            right[i] = prod
            prod *= nums[i]

        for i in range(len(nums)):
            result[i] = right[i]*left[i]

        return result


nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

sol = Solution()
print(sol.productExceptSelf(nums))
