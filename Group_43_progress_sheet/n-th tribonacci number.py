class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        for i in range(3, n+1):
            tri.append(tri[-1] + tri[-2] + tri[-3])
        
        return tri[n]
