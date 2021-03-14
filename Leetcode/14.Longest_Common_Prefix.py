class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        result = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                result.append(x[0])
            else:
                break

        return "".join(result)


strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]
# strs = ["ab", "a"]

sol = Solution()

print(sol.longestCommonPrefix(strs))
