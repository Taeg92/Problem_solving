class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        words = s.strip()
        word_list = words.split(' ')
        return len(word_list[-1])


s = "a "
# Output: 5

sol = Solution()
print(sol.lengthOfLastWord(s))
