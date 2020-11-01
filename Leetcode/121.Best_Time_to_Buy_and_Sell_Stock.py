class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


prices = [7, 1, 5, 3, 6, 4]
# Output: 5

sol = Solution()
print(sol.maxProfit(prices))
