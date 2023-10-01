class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        max_len = ((ceil(target/sum(nums))+1)*len_nums)
        res = float('inf')
        l, r = 0, 1
        curr_sum = nums[l]
        while r < max_len:
#             print(l, r, res)
            if curr_sum == target:
                res = min(res, r-l)
                curr_sum -= nums[l%len_nums]
                l += 1
            elif curr_sum < target:
                curr_sum += nums[r%len_nums]
                r += 1
            elif curr_sum > target and r-l == 1:
                curr_sum = nums[r%len_nums]
                l += 1
                r += 1
            else:
                curr_sum -= nums[l%len_nums]
                l += 1
                
        if res == float('inf'):
            return -1
        else:
            return res
