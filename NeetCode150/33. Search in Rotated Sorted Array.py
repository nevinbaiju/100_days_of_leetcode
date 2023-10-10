class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
#             print(nums[l:r+1], mid)
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid] :
                if target >= nums[l] and target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        mid = (l+r)//2
#         print(l, r, mid)
        return l if nums[mid] == target else -1
                
