class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_pals = 0
        for num in range(97, 123):
            char = chr(num)
            left = s.find(char)
            if left != -1:
                unique_pals += len(set(s[left + 1: s.rfind(char)]))
        
        return unique_pals