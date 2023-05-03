class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        in_bound = lambda x, y : 0 <= x < n and 0 <= y < n
        
        def dfs(i, j):
            que.append((i, j))
            visited.add((i, j))
            for x, y in DIRECTIONS:
                x += i
                y += j
                if in_bound(x, y) and grid[x][y] and (x, y) not in visited:
                    dfs(x, y)
        

        n = len(grid)
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        que = deque()
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    break
            
            if que:
                break
        
        island_dist = 0
        while que:
            for _ in range(len(que)):
                i, j = que.popleft()
                for x, y in DIRECTIONS:
                    x += i
                    y += j
                    if in_bound(x, y) and grid[x][y] and (x, y) not in visited:
                        return island_dist
                    elif in_bound(x, y) and not grid[x][y]:
                        grid[x][y] = 1
                        que.append((x, y))
                        visited.add((x, y))
            
            island_dist += 1
