class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        res = (0, 0)
        res_len = float('inf')
        have = 0
        need = len(set(t))
        t_map = {}
        window_map = {}
        for letter in t:
            t_map[letter] = t_map.get(letter, 0) + 1
        l = r = 0
        while r < len(s):
            letter = s[r]
            if letter in t_map:
                window_map[letter] = window_map.get(letter, 0) + 1
                if window_map[letter] == t_map[letter]:
                    have += 1
                    while have == need:
                        if len(s[l:r]) + 1 < res_len:
                            res = (l, r)
                            res_len = r-l + 1
                        letter = s[l]
                        if letter in t_map:
                            window_map[letter] = window_map[letter] - 1
                            if window_map[letter] < t_map[letter]:
                                have -= 1
                        l += 1
            r += 1
        if res_len == float('inf'):
            return ""
        else:
            return s[res[0]: res[1]+1]
                            
