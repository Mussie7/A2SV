class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for st in s:
            if st.isalnum():
                new_s += st.lower()

        l, r = 0, len(new_s)-1
        while l < r:
            if new_s[l] != new_s[r]:
                return
            l += 1
            r -= 1
        
        return True
