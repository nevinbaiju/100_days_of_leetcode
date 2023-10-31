class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        curr_index = len(digits)-1
        while carry and curr_index > -1:
            curr_sum = digits[curr_index] + carry
            digits[curr_index] = curr_sum % 10 
            carry = curr_sum // 10
            curr_index -= 1
        return [1] + digits if carry else digits
