from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        for i in range(len(prices)-1):
            current_price = prices[i]
            if (current_price < prices[i+1]):
                profits += prices[i+1] - current_price
        return profits