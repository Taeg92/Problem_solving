class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = pow(x, n)

        if result > pow(2, 31) - 1:
            result = pow(2, 31) - 1
        elif result < -pow(2, 31):
            result = -pow(2, 31)
        return result


x = 2.00000
n = 10

sol = Solution()

print(sol.myPow(x, n))
