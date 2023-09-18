class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(curr, prev_copy):
            if curr > n:
                return inf
            
            if curr == n:
                return 0

            if prev_copy == 0:
                return dp(curr + curr, curr) + 2
            return min(dp(curr + prev_copy, prev_copy) + 1, dp(curr + curr, curr) + 2)
        
        return dp(1, 0)
