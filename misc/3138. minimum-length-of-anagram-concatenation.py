from collections import Counter
class Solution:
    def minAnagramLength(self, s: str) -> int:
        str_len = len(s)
        min_val = str_len
        for i in range(str_len//2, 1, -1):
#             print(i)
            if str_len%i == 0:
                ref_counter = Counter(s[:i])
                correct = True
#                 print(s[:i], ref_counter)
                for j in range(i, str_len, i):
                    if Counter(s[j:j+i]) != ref_counter:
                        correct = False
                        break
                if correct:
#                     print("Correct")
                    min_val = i
        return min_val
