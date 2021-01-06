import collections


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        freqs = collections.defaultdict(int)
        count = 0
        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count


sol = Solution()

jewels = "aA"
stones = "aAAbbbb"
# Output: 3

print(sol.numJewelsInStones(jewels, stones))
