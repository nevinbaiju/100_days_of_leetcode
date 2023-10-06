class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        prev = 0
        window, max_window = 0, 1 if nums else 0
        # print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                window = i-prev+1
                # print(prev, i, nums[prev: i+1], window)
                max_window = max(max_window, window)
            else:
                prev = i
        return max_window
