class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = curr_sum
        
        for i in range(1, len(nums)):
            if nums[i] > curr_sum+nums[i]:
                curr_sum = nums[i]
                max_sum = max(curr_sum, max_sum)
            else:
                curr_sum = nums[i] + curr_sum
                max_sum = max(curr_sum, max_sum)
        
        return max_sum
