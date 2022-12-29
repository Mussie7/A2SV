class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        column_ones = [0] * n
        row_ones = [0] * m
        diff = [[0 for j in range(n)] for i in range(m)]
        
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    column_ones[j] += 1
        
        for i in range(m):
            row_ones[i] = grid[i].count(1)

        for i in range(m):
            row_zeroes = n - row_ones[i]

            for j in range(n):
                column_zeroes = m - column_ones[j]
                diff[i][j] = row_ones[i] + column_ones[j] - column_zeroes - row_zeroes
        
        return diff
