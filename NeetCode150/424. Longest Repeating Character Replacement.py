class Solution:
    def get_max_char(self, char_dict):
        max_char = None
        max_num = 0
        for key in char_dict.keys():
            if char_dict[key] > max_num:
                max_num = char_dict[key]
                max_char = key
        
        return max_char

    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        window_end = 0
        
        char_dict = {}
        max_substring = 0

        while window_end < len(s):
            # print(s[window_start: window_end], window_start, window_end, char_dict)
            char_dict[s[window_end]] = char_dict.get(s[window_end], 0) + 1
            maj_char = self.get_max_char(char_dict)
            while ((window_end - window_start + 1) - char_dict[maj_char] ) > k:
                char_dict[s[window_start]] -= 1
                window_start += 1
                maj_char = self.get_max_char(char_dict)
            window_end += 1
            max_substring = max(max_substring, window_end-window_start)

        return max_substring

