class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0

        check = haystack.split(needle)

        if check[0] == haystack:
            return -1
        return len(check[0])


haystack = "hello"
needle = "ll"

sol = Solution()

print(sol.strStr(haystack, needle))
