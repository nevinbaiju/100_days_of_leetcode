class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = (l+r)//2
            if nums[mid][1] == target:
                return mid
            elif target < nums[mid][1]:
                r = mid-1
            else:
                l = mid+1
        mid = (l+r)//2
        
        return mid
    
class TimeMap:

    def __init__(self):
        self.key_dict = {}
        
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = (l+r)//2
            if nums[mid][1] == target:
                return mid
            elif target < nums[mid][1]:
                r = mid-1
            else:
                l = mid+1
        mid = (l+r)//2
        
        return mid

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_dict[key] = self.key_dict.get(key, []) + [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        ts_vals = self.key_dict.get(key, [])
        if ts_vals:
            nearest_key = self.search(ts_vals, timestamp)
            key, ts = ts_vals[nearest_key]
            if ts <= timestamp:
                return key
            else:
                key, ts = ts_vals[nearest_key-1]
                if ts <= timestamp:
                    return key
                else:
                    return ""
        else:
            return ""
