class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            val = pow(x, n // 2)
            return val * val * x if n % 2 else val * val
        
        if n < 0:
            x = 1 / x
            n = -n
        return pow(x, n)
