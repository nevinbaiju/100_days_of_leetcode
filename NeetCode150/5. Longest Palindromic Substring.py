class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ans_len = 0
        for i in range(len(s)):
            l = r = i
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > ans_len:
                        ans = s[l:r+1]
                        ans_len = r-l+1
                    l -= 1
                    r += 1
                else:
                    break
                    
            l, r = i, i+1
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > ans_len:
                        ans = s[l:r+1]
                        ans_len = r-l+1
                    l -= 1
                    r += 1
                else:
                    break
        return ans
