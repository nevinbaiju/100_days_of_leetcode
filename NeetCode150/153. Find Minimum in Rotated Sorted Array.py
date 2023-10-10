class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = float('inf')
        while l < r:
            mid = (l+r) //2
            res = min(res, nums[mid])
            # print(l, r)
            # print(nums[l:r+1], nums[mid])
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return min(res, nums[l])
