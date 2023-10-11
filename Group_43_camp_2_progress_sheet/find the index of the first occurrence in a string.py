class Solution:
    # rabin karp implementation
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)
        if m > n:
            return -1

        ALPHA = 27
        PRIME = 1000000007
        POWERS = [pow(ALPHA, i, PRIME) for i in range(m)]
        OFFSET = ord('a') - 1

        target = 0
        curr_subarray = 0
        for i in range(m):
            idx = ord(needle[i]) - OFFSET
            target += pow(idx * POWERS[m - i - 1], 1, PRIME)
            idx = ord(haystack[i]) - OFFSET
            curr_subarray += pow(idx * POWERS[m - i - 1], 1, PRIME)
            
            target %= PRIME
            curr_subarray %= PRIME

        left, right = 0, m
        while right < n:
            if curr_subarray == target:
                return left
            else:
                idx = ord(haystack[left]) - OFFSET
                curr_subarray -= pow(idx * POWERS[m - 1], 1, PRIME)
                left += 1

            curr_subarray = pow(curr_subarray * ALPHA + (ord(haystack[right]) - OFFSET), 1, PRIME)
            right += 1

        if curr_subarray == target:
            return left
        return -1



    # KMP algorithm implementation
    def strStr(self, haystack: str, needle: str) -> int:
            needleLength, haystackLength = len(needle), len(haystack)
            lps = [0] * needleLength
            m, i = 0, 1
            while i < needleLength:
                if needle[i] == needle[m]:
                    m += 1
                    lps[i] = m
                    i += 1
                elif m > 0:
                    m = lps[m - 1]
                else:
                    i += 1
            
            i, j = 0, 0
            while j < haystackLength:
                if haystack[j] == needle[i]:
                    i += 1
                    j += 1
                elif i > 0:
                    i = lps[i - 1]
                else:
                    j += 1
                
                if i == needleLength:
                    return j - needleLength
            return -1
