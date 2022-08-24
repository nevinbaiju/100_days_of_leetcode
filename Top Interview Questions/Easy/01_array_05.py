from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0

        for num in nums:
            single_num ^= num
        
        return single_num


if __name__ == '__main__':
    params = [1, 1, 2, 3, 2, 3, 5]
    s = Solution()
    print(s.singleNumber(params))