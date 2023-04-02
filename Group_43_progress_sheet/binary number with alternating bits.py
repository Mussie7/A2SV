class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        mask = 1
        curr = n & mask > 0
        while mask << 1 < n:
            mask <<= 1
            prev = curr
            curr = n & mask > 0
            if curr == prev:
                return False
        
        return True
