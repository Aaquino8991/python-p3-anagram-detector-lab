class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [w for w in word_list if self._are_anagrams(self.word, w.lower())]

    def _are_anagrams(self, word1, word2):
        return sorted(word1) == sorted(word2)