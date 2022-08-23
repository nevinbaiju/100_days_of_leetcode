import enum
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            item = nums.pop()
            nums.insert(0, item)
        return nums

class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = []
        len_arr = len(nums)
        k = k % len_arr
        for i in range(k):
            new_nums.append(nums[i])
            nums[i] = nums[-k+i]
        print(new_nums)
        for i, item in enumerate(new_nums):
            try:
                nums[i+k] = item 
            except IndexError:
                print(i, k, i+k)
                print(nums)
                exit()
        
        return nums


if __name__ == '__main__':
    for i in range(3):
        params = ([1, 2, 3, 4, 5, 6], i)
        s = Solution2()
        print(s.rotate(*params))
        