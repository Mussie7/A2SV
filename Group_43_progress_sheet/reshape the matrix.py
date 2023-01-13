class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        new_mat = [[0 for _ in range(c)] for _ in range(r)]

        for index in range(r*c):
            i, j = index // len(mat[0]), index % len(mat[0])
            row, col = index // c, index % c
            
            new_mat[row][col] = mat[i][j]
        
        return new_mat
