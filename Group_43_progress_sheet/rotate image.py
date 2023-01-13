class Solution:
    def reverse(self, row):
        left, right = 0, len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            
            left += 1
            right -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            j = n-1
            while j > i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j -= 1
                
            self.reverse(matrix[i])
