class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[i, j]
            if i == len_s and j == len_p:
                dp[i, j] = True
            elif j >= len_p:
                dp[i, j] = False
            elif i>= len_s:
                if j <= len_p-2 and p[j+1] == '*':
                    dp[i, j] = dfs(i, j+2)
                else:
                    dp[i, j] = False
            else:
                ans = False
                if j <= len_p-2 and p[j+1] == '*':
                    if s[i] == p[j] or p[j] == '.':
                        ans = dfs(i+1, j) or dfs(i+1, j+2)
                    ans = ans or dfs(i, j+2)
                else:
                    if s[i] == p[j] or p[j] == '.':
                        ans = dfs(i+1, j+1)
                dp[i, j] = ans
            return dp[i, j]
        
        return dfs(0, 0)
