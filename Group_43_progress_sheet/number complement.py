class Solution:
    def findComplement(self, num: int) -> int:
        bitmask = 1
        while bitmask <= num:
            num ^= bitmask
            bitmask <<= 1
        
        return num
