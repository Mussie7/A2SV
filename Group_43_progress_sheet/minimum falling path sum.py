class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # a row for memoization
        memo = matrix[0].copy()
        for i in range(1, m):
            curr = []
            for j in range(n):
                # edge cases for when the element is in the first and last column
                if j == 0:
                    curr.append(matrix[i][j] + min(memo[j], memo[j+1]))
                elif j == n-1:
                    curr.append(matrix[i][j] + min(memo[j-1], memo[j]))
                else:
                    curr.append(matrix[i][j] + min(memo[j-1], memo[j], memo[j+1]))
            
            memo = curr
      
        return min(memo)
