class Solution:
    def find(self, coor):
        if self.rep[coor] == coor:
            return coor
        self.rep[coor] = self.find(self.rep[coor])
        return self.rep[coor]
    
    def union(self, coor1, coor2):
        rep1, rep2 = self.find(coor1), self.find(coor2)
        if rep1 == rep2:
            return
        
        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]

    def largestIsland(self, grid: List[List[int]]) -> int:
        in_bound = lambda x, y: 0 <= x < n and 0 <= y < n
        DXN = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.rep = {}
        self.rank = {}
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) not in self.rep:
                        self.rep[(i, j)] = (i, j)
                        self.rank[(i, j)] = 1
                    for x, y in DXN:
                        x += i
                        y += j
                        if in_bound(x, y) and grid[x][y] == 1:
                            if (x, y) not in self.rep:
                                self.rep[(x, y)] = (x, y)
                                self.rank[(x, y)] = 1
                            self.union((i, j), (x, y))
        
        largest_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    reps = set()
                    island = 1
                    for x, y in DXN:
                        x += i
                        y += j
                        if in_bound(x, y) and grid[x][y] == 1 and self.find((x, y)) not in reps:
                            reps.add(self.find((x, y)))
                            island += self.rank[self.find((x, y))]
                    
                    largest_island = max(island, largest_island)
        
        if largest_island == 0:
            return n * n
        return largest_island
