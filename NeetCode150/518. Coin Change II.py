class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i=0, total=0):
            if total > amount or i==len(coins):
                dp[(i, total)] = 0
                return 0
            elif total == amount:
                dp[(i, total)] = 1
                return 1
            if (i, total) in dp:
                return dp[(i, total)]
            else:
                dp[(i, total)] = dfs(i, total+coins[i])+dfs(i+1, total)
                return dp[(i, total)]
        
        ans = dfs()
        # print(dp)
        return ans
