class Compare(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_list = list(map(str, nums))

        if len(nums) == 1:
            return ''.join(nums_list)
        elif len(nums) == 0:
            return ''
        else:
            sorted_nums = sorted(nums_list, key=Compare)
            if list(set(sorted_nums)) == ['0']:
                return sorted_nums[0]
            return ''.join(sorted_nums)


sol = Solution()

nums = [0, 0, 0, 0, 0]

print(sol.largestNumber(nums))
