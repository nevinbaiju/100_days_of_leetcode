class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1

        len_s = len(s)
        len_t = len(t)
        
        if len_s == len_t:
            for i in range(len_s):
                letter = s[i]
                if s_dict[letter] != t_dict.get(letter, 0):
                    return False
        else:
            return False
        
        return True
