class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            
            curr = left
            while left < right and s[left] == s[curr]:
                left += 1
            
            if left == right:
                return 0

            while right > left and s[right] == s[curr]:
                right -= 1
            
            if left == right:
                return 1
        
        return right - left + 1 if right >= left else 0