class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        max_element = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                nums[i] += nums[i+1]
            max_element = max(max_element, nums[i])
        
        return max_element
