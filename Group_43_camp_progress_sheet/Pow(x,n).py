class Solution:
    def square(self, x:float, n:int, target:int) -> tuple:
        if n >= target:
            return x, n
        
        return self.square(x*x, n*2, target)
    
    def revert(self, x:float, base:float, n:int, target:int) -> float:
        if n == target:
            return x
        
        return self.revert(x/base, base, n-1, target)

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        newNum, power = self.square(x, 1, n)
        return self.revert(newNum, x, power, n)
