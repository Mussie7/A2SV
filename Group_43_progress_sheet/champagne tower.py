class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        for i in range(query_row):
            n = len(dp)
            next_row = [0] * (n + 1)
            for index in range(n):
                curr = (dp[index] - 1) / 2
                next_row[index] += max(0, curr)
                next_row[index + 1] += max(0, curr)
            
            dp = next_row
        
        return min(dp[query_glass], 1)
