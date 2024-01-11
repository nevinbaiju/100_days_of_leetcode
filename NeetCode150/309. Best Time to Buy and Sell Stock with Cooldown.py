class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i=0, buying=False):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                dp[(i, buying)] = max(prices[i]+dfs(i+2, False), dfs(i+1, True))
            else:
                dp[(i, buying)] = max(-prices[i]+dfs(i+1, True), dfs(i+1, False))
            return dp[(i, buying)]
                
        return dfs()
