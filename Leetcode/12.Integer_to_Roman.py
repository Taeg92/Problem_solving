class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        num_table = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                     90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        result = ""

        while num > 0:
            for val in num_table:
                if num - val >= 0:
                    result += num_table[val]
                    num -= val
                    break

        return result


num = 1994
# Output: "MCMXCIV"

sol = Solution()

print(sol.intToRoman(num))
