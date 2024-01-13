class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        dp = {}
        def dfs(i=0, j=0, ans=""):
            if (i, j) in dp:
                return dp[i, j]
            if i==l1 and j == l2 and i+j == l3:
                dp[i,j] = True
                return True
            ans = False
            if i+j < l3:
                if i < l1 and s1[i] == s3[i+j]:
                    ans = ans or dfs(i+1, j)
                if j < l2 and s2[j] == s3[i+j]:
                    ans = ans or dfs(i, j+1)
            dp[i, j] = ans
            return ans
        return dfs()
