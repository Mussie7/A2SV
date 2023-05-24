class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        
        # path compression
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        if rep1 == rep2:
            return
        
        # union by rank
        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
            self.cols[rep1].update(self.cols[rep2])
            del self.cols[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]
            self.cols[rep2].update(self.cols[rep1])
            del self.cols[rep1]

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        in_bound = lambda x, y: 0 <= x < row and 0 <= y < col
        dxn = [-1, 0, 1, 0, -1, -1, 1, 1, -1]

        self.rep = {}
        self.rank = {}
        self.cols = defaultdict(set)
        for day, cell in enumerate(cells):
            cell = tuple(cell)
            self.rep[cell] = cell
            self.rank[cell] = 1
            self.cols[cell].add(cell[1])

            for i in range(8):
                x, y = cell[0] + dxn[i], cell[1] + dxn[i + 1]
                if in_bound(x-1, y-1) and (x, y) in self.rep:
                    self.union(cell, (x, y))
            
            # the trick is in knowing when to quit. And that is when 8 directionally connected floods are spread through all the columns
            # that means when one group consisits of atleast one cell from all columns
            if len(self.cols[self.find(cell)]) == col:
                return day
