class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transpose = [[0 for col in range(m)] for row in range(n)]
        for i in range(n):
            for j in range(m):
                transpose[i][j] = matrix[j][i]
        
        return transpose
