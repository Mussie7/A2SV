class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(cell, path):
            if cell == end:
                return int(len(path) == empty_squares_count)

            i, j = cell
            paths_count = 0
            for x, y in DXN:
                x += i
                y += j
                if in_bound(x, y) and (x, y) not in path:
                    path.add((x, y))
                    paths_count += dfs((x, y), path)
                    path.remove((x, y))
            
            return paths_count


        
        in_bound = lambda i, j: 0 <= i < m and 0 <= j < n and grid[i][j] != -1
        m, n = len(grid), len(grid[0])
        DXN = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        empty_squares_count = m * n
        start = end = (-1, -1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    empty_squares_count -= 1
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
        
        return dfs(start, {start})