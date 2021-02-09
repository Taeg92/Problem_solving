class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


sol = Solution()

n = 11
# Output: 3

print(sol.hammingWeight(n))
