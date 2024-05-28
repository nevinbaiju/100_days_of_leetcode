class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n)-1)
        if re.fullmatch(r'10+', n):
            return str(int(n)-1)
        if re.fullmatch(r'9+', n):
            return str(int(n)+2)
        if re.fullmatch(r'10*1', n):
            return str(int(n)-2)
        even = len(n)%2 == 0
        palin_root = n[:len(n)//2] if even else n[:len(n)//2+1]
        reverse = palin_root[::-1] if even else palin_root[-2::-1]
        
        palin_root = str(int(palin_root) + 1)
        reverse = palin_root[::-1] if even else palin_root[-2::-1]
        ans = int(palin_root + reverse)
        
        palin_root = str(int(palin_root) - 1)
        reverse = palin_root[::-1] if even else palin_root[-2::-1]
        ans2 = int(palin_root+reverse)
        
        palin_root = str(int(palin_root) - 1)
        reverse = palin_root[::-1] if even else palin_root[-2::-1]
        ans3 = int(palin_root+reverse)
        
        n = int(n)
        
        if (ans2 != n) and abs(ans2 - n) <= abs(ans - n):
            ans = ans2
        if abs(ans3 - n) <= abs(ans - n):
            ans = ans3
        
        return str(ans)
