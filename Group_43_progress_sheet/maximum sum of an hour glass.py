class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            if i + 2 >= m:
                    break
            for j in range(n):
                if j + 2 >= n:
                    break
                ans = max(ans, sum(grid[i][j:j+3]) + sum(grid[i+2][j:j+3]) + grid[i+1][j+1])
        
        return ans
