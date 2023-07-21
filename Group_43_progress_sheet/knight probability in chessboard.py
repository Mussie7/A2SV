class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dp(row, col, k):
            if not k:
                return 1

            probability = 0
            for x, y in DIRECTION:
                x += row
                y += col
                if in_bound(x, y):
                    probability += dp(x, y, k-1) * 0.125
            
            return probability

        in_bound = lambda r, c: 0 <= r < n and 0 <= c < n
        DIRECTION = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        
        return dp(row, column, k)
