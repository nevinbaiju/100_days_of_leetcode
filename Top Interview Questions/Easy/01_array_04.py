from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_set = dict()
        for item in nums:
            count = unique_set.get(item, 0)
            unique_set[item] = count + 1
            if count:
                return True
        
        return False


if __name__ == '__main__':
    params = [1, 2, 3, 4, 5, 1]
    s = Solution()
    print(s.containsDuplicate(params))