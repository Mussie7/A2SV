class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    memo[i][j] = 1
                elif i == 0:
                    memo[i][j] += memo[i][j-1]
                elif j == 0:
                    memo[i][j] += memo[i-1][j]
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]

        return memo[m-1][n-1]
