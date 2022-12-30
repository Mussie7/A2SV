class Solution:
    def population_director(self, i, dynamic, size1, size2, step, mat):
        while i < size1 and dynamic >= 0:
            if dynamic >= size2:
                dynamic = size2 - 1
                i = step - size2
            
            if step % 2:
                self.output.append(mat[dynamic][i])
            else:
                self.output.append(mat[i][dynamic])
            
            dynamic -= 1
            i += 1

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        step = 1
        self.output = []
        
        for step in range(1, m + n):
            dynamic = step - 1
            i = 0
            
            if step % 2:
                self.population_director(i, dynamic, n, m, step, mat)
            else:
                self.population_director(i, dynamic, m, n, step, mat)

        return self.output
