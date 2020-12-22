class Solution(object):

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x


n = 3
# Output: 2

sol = Solution()

print(sol.fib(n))
