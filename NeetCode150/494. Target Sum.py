class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i=0, total=0):
            if (i, total) in dp:
                return dp[i, total]
            if i == len(nums):
                if total == target:
                    dp[i, total] = 1
                    return 1
                else:
                    dp[i, total] = 0
                    return 0
            else:
                dp[i, total] = dfs(i+1, total-nums[i]) + dfs(i+1, total+nums[i])
                return dp[i, total]
        return dfs()
