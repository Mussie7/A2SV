class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        in_bound = lambda i, j : 0 <= i < m and 0 <= j < n and maze[i][j] != "+"
        is_exit = lambda i, j : (i == 0 or j == 0 or i == m - 1 or j == n - 1) and [i, j] != entrance
        
        m, n = len(maze), len(maze[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        que = deque([entrance + [0]])
        visited = {tuple(entrance)}
        while que:
            i, j, steps = que.popleft()
            if is_exit(i, j):
                return steps
            
            for x, y in DIRECTIONS:
                x += i
                y += j
                if in_bound(x, y) and (x, y) not in visited:
                    visited.add((x, y))
                    que.append([x, y, steps + 1])
        
        return -1
