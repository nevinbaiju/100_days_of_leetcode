class Solution:
    def _rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) > 2:
            nums[2] += nums[0]
            for i in range(3, len(nums)):
                nums[i] = nums[i]+max(nums[i-2], nums[i-3])

        return max(nums[-1], nums[-2])
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))
