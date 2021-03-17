class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_table = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                       'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        pos = 0
        result = 0

        while pos < len(s):

            if (pos + 1) != len(s) and s[pos] + s[pos + 1] in roman_table:
                result += roman_table[s[pos] + s[pos + 1]]
                pos += 2
            else:
                result += roman_table[s[pos]]
                pos += 1

        return result


s = "MCMXCIV"
# Output: 1994

sol = Solution()

print(sol.romanToInt(s))
