class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        inbound = lambda i, j : 0 <= i < m and 0 <= j < n
        def dfs(i, j, curr_gold):
            nonlocal max_gold
            max_gold = max(max_gold, curr_gold)

            for x, y in DXN:
                x += i
                y += j
                if inbound(x, y) and grid[x][y] != 0:
                    cell_gold = grid[x][y]
                    grid[x][y] = 0
                    dfs(x, y, curr_gold + cell_gold)
                    grid[x][y] = cell_gold
        
        m, n = len(grid), len(grid[0])
        DXN = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    cell_gold = grid[i][j]
                    grid[i][j] = 0
                    dfs(i, j, cell_gold)
                    grid[i][j] = cell_gold
        
        return max_gold