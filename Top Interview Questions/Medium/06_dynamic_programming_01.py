from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        
        if last_index == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    params = [3,2,1,0,4]
    print(s.canJump(params))
