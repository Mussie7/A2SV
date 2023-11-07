class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def dp(soupA, soupB):
            if soupA <= 0 and soupB <= 0:
                return 0.5
            elif soupA <= 0:
                return 1
            elif soupB <= 0:
                return 0
            
            possibility = 0
            for a, b in [(100, 0), (75, 25), (50, 50), (25, 75)]:
                possibility += dp(soupA - a, soupB - b) * 0.25
            
            return possibility

        if n > 5000:
            return 1
        
        return dp(n, n)