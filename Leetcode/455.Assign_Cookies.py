class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1

        return i


sol = Solution()

g = [1, 2, 3]
s = [1, 1]
# Output: 1


print(sol.findContentChildren(g, s))
