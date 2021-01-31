class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(level, letters):

            if len(letters) == len(digits):
                result.append(letters)
                return

            for i in range(level, len(digits)):
                for alpha in table[digits[i]]:
                    dfs(i + 1, letters + alpha)

        if not digits:
            return []

        table = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []

        dfs(0, "")

        return result


digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

sol = Solution()
print(sol.letterCombinations(digits))
