class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count_chars = {}
        for letter in s:
            count_chars[letter] = count_chars.get(letter, 0) + 1
        l = -1
        curr_set = set()
        exhausted_set = set()
        ans = []
        for i, letter in enumerate(s):
            count_chars[letter] -= 1
            curr_set.add(letter)
            if not count_chars[letter]:
                exhausted_set.add(letter)
                if len(curr_set) == len(exhausted_set):
                    ans.append(i-l)
                    l = i
                    curr_set = set()
                    exhausted_set = set()
        return ans
