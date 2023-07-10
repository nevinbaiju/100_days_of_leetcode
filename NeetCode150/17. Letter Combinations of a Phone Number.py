class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans = []
        
        def dfs(digits=digits, res_str=""):
            if not digits:
                if res_str:
                    ans.append(res_str)
            else:
                letters = letter_map[digits[0]]
                for letter in letters:
                    res_str += letter
                    dfs(digits[1:], res_str)
                    res_str = res_str[:-1]
                    
        dfs()
        return ans
