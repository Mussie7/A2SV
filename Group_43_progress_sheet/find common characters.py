class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        charArray = [0] * 26
        offset = ord('a')
        
        original_letters = Counter(words[0])
        for char, count in original_letters.items():
            charArray[ord(char) - offset] = count

        for i in range(1, len(words)):
            letters = Counter(words[i])

            # this block of code helps track the letters in the first word
            for letter in list(original_letters.keys()):
                if letter not in letters:
                    charArray[ord(letter) - offset] = 0
                    del original_letters[letter]

            # for letters that come starting from the second word take the minimum between the current count of occurence and the previous
            for char, count in letters.items():
                cur = ord(char) - offset
                charArray[cur] = min(count, charArray[cur])
        
        # append all the common characters and their duplicates
        commonChars = []
        for ascii in range(len(charArray)):
            commonChars.extend([chr(offset + ascii)] * (charArray[ascii]))
        
        return commonChars
