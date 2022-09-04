from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i, item in enumerate(nums):
            index_dict[item] = i
        
        for i, item in enumerate(nums):
            required_num = target - item
            index_second = index_dict.get(required_num, -1)

            if ((index_second != -1) and (index_second != i)):
                return i, index_second



if __name__ == '__main__':
    params = ([0,1,0,3,12], 13)
    s = Solution()
    print(s.twoSum(*params))
        