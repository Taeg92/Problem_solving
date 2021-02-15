class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


sol = Solution()

x = 1
y = 4
# Output: 2

print(sol.hammingDistance(x, y))
