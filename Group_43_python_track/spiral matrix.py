class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = j = 0
        spiral = []
        
        for _ in range(math.ceil(m / 2)):
            for dir in DIRECTION:
                if matrix[i][j] == -111:
                    i += dir[0]
                    j += dir[1]

                while 0 <= i < m and 0 <= j < n and matrix[i][j] != -111:
                    spiral.append(matrix[i][j])
                    matrix[i][j] = -111
                    
                    i += dir[0]
                    j += dir[1]

                
                i -= dir[0]
                j -= dir[1]
        
        return spiral
