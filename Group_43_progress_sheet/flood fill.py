class Solution:
    def in_bound(self, i, j):
        return 0 <= i < len(self.image) and 0 <= j < len(self.image[0])

    def dfs(self, i, j):
        self.image[i][j] = self.color
        for x, y in self.DIRECTION:
            x += i
            y += j
            if self.in_bound(x, y) and self.image[x][y] == self.before:
                self.dfs(x, y)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.before = image[sr][sc]
        self.image = image
        self.color = color
        self.DIRECTION = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        
        if self.color != self.before:
            self.dfs(sr, sc)
        return self.image
