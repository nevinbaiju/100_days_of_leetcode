class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window_start = 0
        window_end = 1
        profit = 0
        while window_end < len(prices):
            # print(prices[window_start], prices[window_end])
            if prices[window_start] > prices[window_end]:
                window_start = window_end
                window_end += 1
            else:
                profit = max(profit, prices[window_end]-prices[window_start])
                window_end += 1

        return profit
