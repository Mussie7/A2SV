from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_dic = defaultdict(int)

        for row in grid:
            row_dic[tuple(row)] += 1
        
        equal_pairs = 0
        
        for i in range(n):
            column = [grid[j][i] for j in range(n)]
            equal_pairs += row_dic[tuple(column)]
        
        return equal_pairs
