class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        offset = ord('a')
        char_arrayP = [0] * 26
        for char in p:
            char_arrayP[ord(char)-offset] += 1
        
        start = 0
        char_arrayS = [0] * 26
        anagram_indices = []
        for end in range(len(s)):
            char_arrayS[ord(s[end])-offset] += 1
            
            if end >= len(p)-1:
                if char_arrayS == char_arrayP:
                    anagram_indices.append(start)
                char_arrayS[ord(s[start])-offset] -= 1
                start += 1

        return anagram_indices            
