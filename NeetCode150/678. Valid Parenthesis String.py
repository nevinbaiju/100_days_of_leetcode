class Solution:
    def checkValidString(self, s: str) -> bool:
        l_max = l_min = 0
        
        for para in s:
            if para == '(':
                l_max += 1
                l_min += 1
            elif para == ')':
                l_min -= 1
                l_max -= 1
            else:
                l_min -= 1
                l_max += 1
            if l_max < 0:
                return False
            l_min = max(0, l_min)
        return l_min == 0
