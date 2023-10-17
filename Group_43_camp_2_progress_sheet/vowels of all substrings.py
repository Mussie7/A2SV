class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i, char in enumerate(word):
            if char in vowels:
                count += (i + 1) * (n - i)
        
        return count
