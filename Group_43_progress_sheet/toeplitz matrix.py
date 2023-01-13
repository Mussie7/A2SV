class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonal = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j in diagonal and diagonal[i-j] != matrix[i][j]:
                    return False
                
                diagonal[i-j] = matrix[i][j]
        
        return True
