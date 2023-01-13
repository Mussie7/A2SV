class Solution:
    def findMax(self, grid, DIRECTION, point) -> int:
        i, j = point
        current = grid[i][j]
        
        for dxn in DIRECTION:
            current = max(grid[i+dxn[0]][j+dxn[1]], current)
        
        return current

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        largest = []
        DIRECTION = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

        for i in range(1, n-1):
            row = []
            for j in range(1, n-1):
                row.append(self.findMax(grid, DIRECTION, (i, j)))
            
            largest.append(row)
        
        return largest    
