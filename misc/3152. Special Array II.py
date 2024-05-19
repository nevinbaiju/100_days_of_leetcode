class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> bool:
        curr = nums[0]
        nums[0] = 0
        for i in range(1, len(nums)):
            if ((curr % 2) == 0 and (nums[i] % 2) == 0) or ((curr % 2) != 0 and (nums[i] % 2) != 0):
                ans = nums[i-1] + 1
            else:
                ans = nums[i-1]
            curr = nums[i]
            nums[i] = ans
        ans = []
        for start, end in queries:
            if nums[start] != nums[end]:
                ans.append(False)
            else:
                ans.append(True)
        return ans
