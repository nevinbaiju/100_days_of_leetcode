class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        word_len = len(processed_str)
        for i in range(word_len//2):
            if processed_str[i] != processed_str[word_len-i-1]:
                return False
        
        return True
