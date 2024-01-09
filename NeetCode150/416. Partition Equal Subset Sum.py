class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        sum_set = set()
        for i in range(len(nums)-1, -1, -1):
            for sum_val in list(sum_set):
                if nums[i] == target or nums[i] + sum_val == target:
                    return True
                else:
                    sum_set.add(nums[i] + sum_val)
            sum_set.add(nums[i])
        return False
