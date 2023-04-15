class Solution:
    def in_bound(self, i, j):
        m, n = len(self.grid2), len(self.grid2[0])
        return 0 <= i < m and 0 <= j < n and self.grid2[i][j]

    def dfs(self, i, j):
        if not self.grid1[i][j]:
            self.is_sub_island = False
        
        for x, y in self.DIRECTION:
            x += i
            y += j
            if self.in_bound(x, y):
                self.grid2[x][y] = 0
                self.dfs(x, y)
        
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.DIRECTION = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        self.grid1, self.grid2 = grid1, grid2
        sub_islands_count = 0
        for i in range(len(self.grid2)):
            for j in range(len(self.grid2[0])):
                if self.grid2[i][j]:
                    self.is_sub_island = True
                    self.grid2[i][j] = 0
                    self.dfs(i, j)
                    sub_islands_count += self.is_sub_island

        return sub_islands_count
