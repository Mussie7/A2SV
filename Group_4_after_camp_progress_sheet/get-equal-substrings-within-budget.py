class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        max_substring_len = 0
        curr_cost = 0
        for right in range(len(s)):
            curr_cost += abs(ord(s[right]) - ord(t[right]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            max_substring_len = max(max_substring_len, right - left + 1)
        
        return max_substring_len