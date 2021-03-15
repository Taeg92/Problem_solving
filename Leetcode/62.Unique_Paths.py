class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def factorial(n):
            val = 1

            while n >= 1:
                val *= n
                n -= 1

            return val

        return factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1))


m = 3
n = 7
# Output: 28

sol = Solution()

print(sol.uniquePaths(m, n))
