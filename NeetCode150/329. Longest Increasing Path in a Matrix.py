class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        h, w = len(matrix), len(matrix[0])
        dp = [[-1]*w for i in range(h)]
        def dfs(i, j):
            if dp[i][j] == -1:
                ans = -1
                if i+1 < h and matrix[i][j] < matrix[i+1][j]:
                    ans = max(ans, dfs(i+1, j))
                if i-1 > -1 and matrix[i][j] < matrix[i-1][j]:
                    ans = max(ans, dfs(i-1, j))
                if j+1 < w and matrix[i][j] < matrix[i][j+1]:
                    ans = max(ans, dfs(i, j+1))
                if j-1 > -1 and matrix[i][j] < matrix[i][j-1]:
                    ans = max(ans, dfs(i, j-1))
                dp[i][j] = 1+ans
                return 1+ans
            else:
                return dp[i][j]
            
        ans = 0
        for i in range(h):
            for j in range(w):
                ans = max(ans, dfs(i, j))
        return ans+1
