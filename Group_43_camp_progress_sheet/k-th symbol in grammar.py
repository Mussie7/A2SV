class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return k-1

        if k <= 2**(n-2):
            return self.kthGrammar(n-1, k)
        if k <= (2**(n-2) + 2**(n-3)):
            return self.kthGrammar(n-1, 2**(n-3) + (k - 2**(n-2))) 
        return self.kthGrammar(n-1, k - (2**(n-2) + 2**(n-3)))
