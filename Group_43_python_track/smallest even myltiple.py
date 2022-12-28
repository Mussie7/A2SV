class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # so that I don't have to use modulo
        if n == (n//2) * 2:
            return n
        
        return n * 2
