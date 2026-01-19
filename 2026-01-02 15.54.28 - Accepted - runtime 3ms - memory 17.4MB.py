class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        def almost_equal(a, b):
            return abs(ord(a) - ord(b)) <= 1
        
        n = len(word)
        count = 0
        i = 0
        
        while i < n - 1:
            if almost_equal(word[i], word[i + 1]):
                # Change word[i+1], then skip to i+2
                count += 1
                i += 2
            else:
                i += 1
        
        return count