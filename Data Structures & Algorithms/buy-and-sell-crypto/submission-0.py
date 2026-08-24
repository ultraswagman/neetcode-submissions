class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit_check = prices[i]- min_price
            if profit_check > max_profit:
                max_profit = profit_check
        return max_profit