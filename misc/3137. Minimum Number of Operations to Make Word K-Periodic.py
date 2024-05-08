class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        word_count = {}
        for i in range(0, len(word), k):
            word_count[word[i: i+k]] = word_count.get(word[i: i+k], 0) + 1
        max_word, max_count = '', 0
        for key in word_count.keys():
            if word_count[key] > max_count:
                max_count = word_count[key]
                max_word = key
        return len(word)//k - max_count
