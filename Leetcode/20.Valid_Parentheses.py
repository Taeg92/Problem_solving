class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        close_table = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in close_table:
                if stack:
                    token = stack.pop()
                    if token != close_table[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return True


sol = Solution()

s = "(){}}{"
# Output: true

print(sol.isValid(s))
