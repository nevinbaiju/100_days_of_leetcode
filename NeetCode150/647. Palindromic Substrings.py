class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            l = r = i
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    ans+= 1

                    l -= 1
                    r += 1
                else:
                    break
                    
            l, r = i, i+1
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    ans += 1
                    
                    l -= 1
                    r += 1
                else:
                    break
        return ans
