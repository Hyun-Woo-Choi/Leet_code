from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_counts = dict(Counter(s))
        word2_counts = dict(Counter(t))

        return word_counts == word2_counts