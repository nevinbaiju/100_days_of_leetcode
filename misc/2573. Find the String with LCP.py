class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        len_lcp = len(lcp)
        ans = [0] * len_lcp
        curr_str = 122
        for i in range(len_lcp-1, -1, -1):
            if curr_str < 96:
                return ''
            if ans[i]:
                continue
            elif i < len_lcp - 2 and lcp[i+1][i]:
                ans[i] = chr(curr_str)
                continue
            else:
                try:
                    ans[i] = chr(curr_str)
                except:
                    print(curr_str)
                curr_str -= 1
            for j in range(i, -1, -1):
                if lcp[i][j]:
                    ans[j] = ans[i]
        char_mapping = {}
        curr_str = 97
        for i, letter in enumerate(ans):
            if letter in char_mapping:
                ans[i] = char_mapping[letter]
            else:
                char_mapping[letter] = chr(curr_str)
                curr_str += 1
                ans[i] = char_mapping[letter]
        if curr_str > 123:
            return ""
        for i in range(len_lcp):
            for j in range(len_lcp):
                v = lcp[i + 1][j + 1] if i + 1 < len_lcp and j + 1 < len_lcp else 0
                v = v + 1 if ans[i] == ans[j] else 0
                if lcp[i][j] != v:
                    return ''
        return "".join(ans)
