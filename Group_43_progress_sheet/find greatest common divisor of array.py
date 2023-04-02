class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = inf, -inf
        for num in nums:
            a, b = min(a, num), max(b, num)

        mod = b % a
        while mod:
            b, a = a, mod
            mod = b % a
        
        return a
