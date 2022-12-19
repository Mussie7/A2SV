class Solution:
    def isPalindrome(self, x: int) -> bool:
        st_x = str(x)
        l, r = 0, len(st_x) - 1
        while l < r:
            if st_x[l] != st_x[r]:
                return
            l += 1
            r -= 1

        return True
