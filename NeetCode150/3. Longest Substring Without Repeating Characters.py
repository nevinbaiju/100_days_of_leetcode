class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        window_end = 0
        char_set = set()
        max_len = 0

        while window_end < len(s):
            while s[window_end] in char_set:
                char_set.remove(s[window_start])
                window_start += 1
            char_set.add(s[window_end])
            window_end += 1
            max_len = max(max_len, window_end - window_start)

        return max_len
