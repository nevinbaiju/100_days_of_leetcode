class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        outer = 0
        len_nums = len(nums)
        sol = []
        while (nums[outer] <= 0) and outer < len_nums-2:
            inner_l = outer+1
            inner_r = len_nums-1
            req_sum = -nums[outer]
            while(inner_l < inner_r):
                curr_sum = nums[inner_l] + nums[inner_r]
                if curr_sum == req_sum:
                    sol.append([nums[outer], nums[inner_l], nums[inner_r]])
                if curr_sum <= req_sum:
                    while(inner_l < len_nums-1 and nums[inner_l] == nums[inner_l+1]):
                        inner_l += 1
                    inner_l += 1
                else:
                    while(inner_r > 1 and nums[inner_r] == nums[inner_r-1]):
                        inner_r -= 1
                    inner_r -= 1
            while(outer < len_nums-2 and nums[outer] == nums[outer+1]):
                outer += 1
            outer += 1
        
        return sol
