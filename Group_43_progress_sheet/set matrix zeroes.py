class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroes = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))
        
        for x, y in zeroes:
            for j in range(n):
                matrix[x][j] = 0
            
            for i in range(m):
                matrix[i][y] = 0
