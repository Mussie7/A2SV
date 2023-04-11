class Solution:
    def valid(self, i, j):
        return 0 <= i < len(self.grid) and 0 <= j < len(self.grid[0]) and self.grid[i][j]

    def dfs(self, i, j):
        count = 1
        for x, y in self.DIRECTION:
            x += i
            y += j
            if self.valid(x, y):
                self.grid[x][y] = 0
                count += self.dfs(x, y)
            
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        max_area = 0
        self.visited = set()
        self.DIRECTION = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j]:
                    self.grid[i][j] = 0
                    max_area = max(max_area, self.dfs(i, j))

        return max_area
