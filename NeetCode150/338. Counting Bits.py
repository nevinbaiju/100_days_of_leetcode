class Solution:
    def countBits(self, n: int) -> List[int]:
        if not n:
            return [0]
        msb = 1
        dp = [0, 1]
        for i in range(2, n+1):
            if i == 2*msb:
                msb *=2
            dp.append(dp[i-msb]+1)
        return dp
