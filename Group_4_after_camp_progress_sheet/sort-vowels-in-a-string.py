class Solution:
    def sortVowels(self, s: str) -> str:
        new_s = list(s)
        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels = []
        for char in new_s:
            if char in VOWELS:
                vowels.append(char)
        
        vowels.sort()
        pointer = 0
        for i, char in enumerate(new_s):
            if char in VOWELS:
                new_s[i] = vowels[pointer]
                pointer += 1
        
        return ''.join(new_s)