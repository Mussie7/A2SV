class Solution:
    def recurse(self, rowIndex, pascalTriangle):
        if rowIndex + 1 == len(pascalTriangle):
            return pascalTriangle
        for i in range(len(pascalTriangle)-1, 0, -1):
            pascalTriangle[i] += pascalTriangle[i-1]
        
        pascalTriangle.append(1)
        return self.recurse(rowIndex, pascalTriangle)

    def getRow(self, rowIndex: int) -> List[int]:
        return self.recurse(rowIndex, [1])
