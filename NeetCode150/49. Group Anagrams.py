class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            signature = [0]*26
            for letter in s:
#                 print(ord(letter)-ord('a'))
                signature[ord(letter)-ord('a')] += 1
            ans[tuple(signature)].append(s)
#         print(ans)
        return ans.values()
