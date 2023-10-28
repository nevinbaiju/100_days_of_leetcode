class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        jumps_required = 1
        for i in range(len_nums-2, -1, -1):
            if nums[i] >=jumps_required:
                jumps_required = 1
                continue
            else:
                jumps_required += 1
        return True if jumps_required <= nums[0] or len_nums == 1 else False
                    
