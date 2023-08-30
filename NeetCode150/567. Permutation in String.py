class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = [0]*26
        s2_map = [0]*26
        matches = 0
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - 97] += 1
            s2_map[ord(s2[i]) - 97] += 1
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1
        window_left = 0
        window_right = len(s1)
        while window_right < len(s2):
#             print(s1_map, s2_map, window_left, window_right)
            if matches == 26:
                return True
            index = ord(s2[window_left]) - 97
            s2_map[index] -= 1
            if s1_map[index] == s2_map[index]:
                matches += 1
            elif s1_map[index] == s2_map[index]+1:
                matches -= 1
            window_left += 1
                        
            index = ord(s2[window_right]) - 97
            s2_map[index] += 1
            if s1_map[index] == s2_map[index]:
                matches += 1
            elif s1_map[index] == s2_map[index]-1:
                matches -= 1
            window_right += 1
            
        
        return matches == 26
