class Solution:
    # KMP algorithm implementation
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # if length of A is greater than B
        # A mustn't be doubled more than once to yield a substring equal to B
        if len(a) > len(b):
            if b in a:
                return 1
            elif b in a + a:
                return 2
            else:
                return -1

        # building the longest prefix-suffix(lps) array
        b_len, a_len = len(b), len(a)
        lps = [0] * b_len
        i, m = 1, 0
        while i < b_len:
            if b[i] == b[m]:
                m += 1
                lps[i] = m
                i += 1
            elif m > 0:
                m = lps[m - 1]
            else:
                i += 1
        
        a_pointer, b_pointer = 0, 0
        found = False
        while a_len < b_len * 2:
            # add the length of A everytime you reset the pointer
            if a_pointer == len(a):
                a_pointer -= len(a)
                a_len += len(a)
            
            if a[a_pointer] == b[b_pointer]:
                a_pointer += 1
                b_pointer += 1
            elif b_pointer > 0:
                b_pointer = lps[b_pointer - 1]
            else:
                a_pointer += 1
            
            if b_pointer == len(b):
                found = True
                break
        
        if found:
            return a_len // len(a)
        return -1
