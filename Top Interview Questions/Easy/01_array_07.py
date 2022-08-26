from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        if not digits[0]:
            digits.insert(0, 1)
        
        return digits

if __name__ == '__main__':
    params = [1,1,9]
    s = Solution()
    print(s.plusOne(params))