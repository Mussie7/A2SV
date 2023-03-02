class Solution:
    def calculatePreSum(self, grid):
        n = len(grid[0])
        # create presum array like grid
        preSum = [[0] * n for _ in range(len(grid))]
        preSum[0][-1] = grid[0][-1]
        
        # calculate presum for the first row from back to front
        for j in range(n-2, -1, -1):
            preSum[0][j] = grid[0][j] + preSum[0][j+1]
        
        # calculate presum for the second row from front to back
        preSum[1][0] = grid[1][0]
        for j in range(1, n):
            preSum[1][j] = grid[1][j] + preSum[1][j-1]
        
        return preSum

    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        preSum = self.calculatePreSum(grid)
        
        row = col = 0
        while col < n:
            # erase the point when collected by player 1
            grid[row][col] = 0
            
            # the moment the lower row becomes larger change the row because we want the worst for player one
            # also when you reach the end of the first column
            if not row and (col == n-1 or (preSum[row+1][col] > preSum[row][col+1])):
                row += 1
            else:
                col += 1
        
        # because we are told their path's cross there is no way player 2 can collect points from both rows so the maximum one is the answer
        return max(sum(grid[0]), sum(grid[1]))
