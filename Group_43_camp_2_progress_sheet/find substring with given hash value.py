class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        # reverse the string so that we don't have to divide the hash when we do sliding window
        s = s[::-1]
        offset = ord('a') - 1
        
        curr_subarray = 0
        for i in range(k):
            idx = ord(s[i]) - offset
            # since the power raised to k could be a large number modulo is crucial
            curr_subarray += pow(idx * pow(power, (k - i - 1), modulo), 1, modulo)
            curr_subarray %= modulo

        left = 0
        ans = -1
        MAX_POWER = pow(power, (k - 1), modulo)
        if curr_subarray == hashValue:
                ans = left
        
        for right in range(k, len(s)):
            # shift the window by one
            idx = ord(s[left]) - offset
            curr_subarray -= pow(idx * MAX_POWER, 1, modulo)
            curr_subarray = pow(curr_subarray * power + (ord(s[right]) - offset), 1, modulo)
            left += 1
        
            if curr_subarray == hashValue:
                ans = left
            
        return s[ans: ans + k][::-1]
