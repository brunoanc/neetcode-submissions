class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            price = prices[i]
            profit = price - lowest_buy

            if profit > max_profit:
                max_profit = profit

            if price < lowest_buy:
                lowest_buy = price

        return max_profit