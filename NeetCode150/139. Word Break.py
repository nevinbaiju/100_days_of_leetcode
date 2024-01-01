class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_list = [len(x) for x in wordDict]
        len_word = len(s)
        
        dp = [False] * (len_word+1)
        dp[-1] = True
        
        for i in range(len(s)-1, -1, -1):
            for j, dict_word in enumerate(wordDict):
                if (i + len_list[j] - 1 < len_word) and s[i: i+len_list[j]] == dict_word and dp[i + len_list[j]]:
#                     print(s[i: i+len_list[j] + 1])
                    dp[i] = True
        return dp[0]
