class Solution:
    def cubeCheck(self, grid):
        c = Counter(grid[0]) + Counter(grid[1]) + Counter(grid[2])
        if set(c.keys()) != {1,2,3,4,5,6,7,8,9}:
            return False
        
        cols = list(zip(*grid))
        majorDiagonal = grid[0][0] + grid[1][1] + grid[2][2]
        minorDiagonal = grid[0][2] + grid[1][1] + grid[2][0]
        
        if not sum(grid[0]) == sum(grid[1]) == sum(grid[2]) == sum(cols[0]) == sum(cols[1]) == sum(cols[2]) == majorDiagonal == minorDiagonal:
            return False
        
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                count += self.cubeCheck([grid[i-1][j-1:j+2], grid[i][j-1:j+2], grid[i+1][j-1:j+2]])

        return count
