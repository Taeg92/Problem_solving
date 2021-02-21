class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(list(map(str, digits))))
        num += 1
        return list(map(int, list(str(num))))


digits = [1, 2, 3]

sol = Solution()

print(sol.plusOne(digits))
