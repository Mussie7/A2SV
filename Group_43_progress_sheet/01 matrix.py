class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        in_bound = lambda i, j : 0 <= i < m and 0 <= j < n
        
        m, n = len(mat), len(mat[0])
        que = deque()
        dist = [[-1] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i, j, 0))
                    dist[i][j] = 0
        
        DIRECTION = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while que:
            cell = que.popleft()
            for x, y in DIRECTION:
                x += cell[0]
                y += cell[1]
                if in_bound(x, y) and dist[x][y] == -1:
                    dist[x][y] = cell[2] + 1
                    que.append((x, y, cell[2] + 1))
        
        return dist
