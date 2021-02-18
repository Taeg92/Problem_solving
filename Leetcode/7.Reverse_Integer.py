class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_num = str(abs(x))

        answer = int(str_num[::-1]) if x >= 0 else -int(str_num[::-1])

        return answer if answer.bit_length() < 32 else 0


x = 123
# Output = 321

sol = Solution()
print(sol.reverse(x))
