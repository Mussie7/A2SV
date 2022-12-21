class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, output = 0, ""
        while l < len(word1) and l < len(word2):
            output += word1[l] + word2[l]
            l += 1
        
        if len(word1) > l:
            output += word1[l:]
        else:
            output += word2[l:]
        
        return output
