class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            max_len = lis[i]
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    lis[i] = max(lis[i], lis[j]+1)
                    
        return max(lis)
