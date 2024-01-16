class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)
        dp = [[0] * (t_len+1) for i in range(s_len+1)]
        
        for i in range(t_len+1):
            dp[s_len][i] = 0
        for i in range(s_len+1):
            dp[i][t_len] = 1
        for i in range(s_len-1, -1, -1):
            for j in range(t_len-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i][j] + dp[i+1][j+1]
                dp[i][j] = dp[i][j] + dp[i+1][j]
        return dp[0][0]
