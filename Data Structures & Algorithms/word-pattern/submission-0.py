class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        letterToWord = {}
        usedWords = set()

        for letter, word in zip(pattern, words):
            if letter in letterToWord:
                if letterToWord[letter] != word:
                    return False
            else:
                if word in usedWords:
                    return False
                letterToWord[letter] = word
                usedWords.add(word)

        return True