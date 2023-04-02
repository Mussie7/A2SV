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
    
    # a very neat code if you ask me
    def hasAlternatingBits(self, n: int) -> bool:
        curr = n & 1
        n >>= 1
        while n:
            if curr == n & 1:
                return False
            curr = n & 1
            n >>= 1
        
        return True
