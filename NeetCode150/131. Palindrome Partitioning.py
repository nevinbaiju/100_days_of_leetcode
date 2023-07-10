class Solution:
    
    def ispalin(self, s):
        return s == s[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        stack = []
        
        
        def dfs(index=0):
            if index == len(s):
                ans.append(list(stack))
                return
            else:
                for j in range(index+1, len(s)+1):
                    sub_str = s[index:j]
                    if self.ispalin(sub_str):
                        stack.append(sub_str)
                        dfs(j)
                        stack.pop()
                    else:
                        continue

        dfs()
        return ans
