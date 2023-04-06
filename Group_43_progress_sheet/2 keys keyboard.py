class Solution:
    def minSteps(self, n: int) -> int:
        old_gcd = 0
        cur = 1
        steps = 0
        while cur < n:
            new_gcd = gcd(cur, n)
            if new_gcd != old_gcd:
                old_gcd = new_gcd
                steps += 2
            else:
                steps += 1
            cur += old_gcd
        
        return steps
