class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def dp(left, right):
            if left > right:
                return 0
            elif left == right:
                return 1
            
            if s[left] == s[right]:
                return dp(left + 1, right - 1) + 2
            return max(dp(left + 1, right), dp(left, right - 1))


        return dp(0, n - 1)
