class Solution:
    def longestPrefix(self, s: str) -> str:
        s_len = len(s)
        lps = [0] * s_len
        i, m = 1, 0
        while i < s_len:
            if s[i] == s[m]:
                m += 1
                lps[i] = m
                i += 1
            elif m > 0:
                m = lps[m - 1]
            else:
                i += 1
        
        return s[:lps[-1]]
