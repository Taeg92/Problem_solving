class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        if len(s) < 2 or s == s[:-1]:
            return s

        for i in range(len(s) - 1):
            result = max(result, self.expand(s, i, i + 1), self.expand(s, i, i + 2), key=len)
        
        return result

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
        
        
        
        
    
s = "babad"
# Output: "bab"

sol = Solution()
print(sol.longestPalindrome(s))