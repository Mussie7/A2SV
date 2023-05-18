class Solution:
    def find(self, i, j):
        if self.rep[i][j] == (i, j):
            return (i, j)
        
        self.rep[i][j] = self.find(*self.rep[i][j])
        return self.rep[i][j]

    def union(self, cell1, cell2):
        i1, j1 = self.find(*cell1)
        i2, j2 = self.find(*cell2)

        if (i1, j1) == (i2, j2):
            return
        
        if self.rank[i1][j1] > self.rank[i2][j2]:
            self.rep[i2][j2] = (i1, j1)
            self.rank[i1][j1] += self.rank[i2][j2]
        else:
            self.rep[i1][j1] = (i2, j2)
            self.rank[i2][j2] += self.rank[i1][j1]

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        in_bound = lambda i, j : 0 <= i < m and 0 <= j < n

        m, n = len(grid), len(grid[0])
        # a map of the direction's coordinates and the streets that fit
        DIRECTION = {'U': [(-1, 0), [2, 3, 4]], 'D': [(1, 0), [2, 5, 6]], 'L': [(0, -1), [1, 4, 6]], 'R': [(0, 1), [1, 3, 5]]}
        # the two ways the streets connect
        street = {1: ['L', 'R'], 2: ['U', 'D'], 3: ['L', 'D'], 4: ['R', 'D'], 5: ['L', 'U'], 6: ['R', 'U']}
        
        # representative and rank for every cell
        self.rep = [[(i, j) for j in range(n)] for i in range(m)]
        self.rank = [[1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for dxn in street[grid[i][j]]:
                    (x, y), lead = DIRECTION[dxn]
                    x, y = x + i, y + j
                    if in_bound(x, y) and grid[x][y] in lead:
                        self.union((i, j), (x, y))
        
        return self.find(0, 0) == self.find(m-1, n-1)
