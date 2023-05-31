# top-down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def path(i, j):
            if i == 0 or j == 0:
                return 1

            if memo[i][j]:
                return memo[i][j]
            
            memo[i][j] = path(i-1, j) + path(i, j-1)
            return memo[i][j]
        
        memo = [[0 for col in range(n)] for row in range(m)]
        return path(m-1, n-1)


# bottom-up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]
        
        return memo[m-1][n-1]
