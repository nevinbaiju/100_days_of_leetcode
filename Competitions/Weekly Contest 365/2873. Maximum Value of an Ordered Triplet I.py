class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        len_nums = len(nums)
        for i in range(len_nums-2):
            for j in range(i+1, len_nums-1):
                if nums[j] > nums[i]:
                    continue
                else:
                    for k in range(j+1, len_nums):
                        res = max(res, (nums[i] - nums[j])*nums[k])
        
        return res
