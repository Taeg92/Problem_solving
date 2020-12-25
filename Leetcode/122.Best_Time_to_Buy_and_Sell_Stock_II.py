class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                answer += prices[i + 1] - prices[i]
        return answer


sol = Solution()

prices = [7, 1, 5, 3, 6, 4]
# Output: 7

print(sol.maxProfit(prices))
