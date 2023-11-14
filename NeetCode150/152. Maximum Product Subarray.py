class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_dp = (len(nums))*[0]
        max_dp = (len(nums))*[0]
        
        min_dp[0] = nums[0]
        max_dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            min_dp[i] = min(min(nums[i], nums[i]*min_dp[i-1]), nums[i]*max_dp[i-1])
            max_dp[i] = max(max(nums[i], nums[i]*max_dp[i-1]), nums[i]*min_dp[i-1])
        return max(max_dp)
