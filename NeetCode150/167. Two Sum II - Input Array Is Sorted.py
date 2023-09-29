class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_ptr = 0
        second_ptr = len(numbers)-1
        
        while first_ptr != second_ptr:
            curr_total = numbers[first_ptr] + numbers[second_ptr]
            if curr_total == target:
                return first_ptr, second_ptr
            elif curr_total > target:
                second_ptr -=1
            else:
                first_ptr += 1
