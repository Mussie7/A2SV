class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(idx1, idx2):
            if idx2 == m:
                return idx1 == n

            ans = False
            if idx2 < m - 1 and p[idx2 + 1] == '*':
                ans |= dp(idx1, idx2 + 2)
                if idx1 < n and (s[idx1] == p[idx2] or p[idx2] == '.'):
                    ans |= dp(idx1 + 1, idx2)
            
            if idx1 < n and s[idx1] == p[idx2] or p[idx2] == '.':
                ans |= dp(idx1 + 1, idx2 + 1)
            
            return ans

        n, m = len(s), len(p)
        return dp(0, 0)