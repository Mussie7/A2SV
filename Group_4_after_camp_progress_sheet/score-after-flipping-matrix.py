class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 1:
                continue
            
            for col_index in range(len(row)):
                row[col_index] = 1 - row[col_index]

        score = 0
        for col_index in range(len(grid[0])):
            ones = 0
            for row_index in range(len(grid)):
                ones += grid[row_index][col_index]
            ones = max(ones, len(grid) - ones)
            score += ones * pow(2, len(grid[0]) - col_index - 1)
        
        return score