class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def burst(l, r):
            if l > r:
                return 0
            if (l, r) not in dp:
                dp[(l, r)] = 0
                for i in range(l, r+1):
                    coins = nums[l-1]*nums[i]*nums[r+1]
                    coins += burst(l, i-1) + burst(i+1, r)
                    dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        return burst(1, len(nums)-2)
