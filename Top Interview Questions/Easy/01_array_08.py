from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeroes = 0
        number_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[number_index] = nums[i]
                number_index += 1
            else:
                num_zeroes +=1
        for i in range(number_index, number_index+num_zeroes):
            nums[i] = 0
        return nums

    def moveZeroesBetter(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pos = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos +=1

if __name__ == '__main__':
    params = [0,1,0,3,12]
    s = Solution()
    print(s.moveZeroes(params))