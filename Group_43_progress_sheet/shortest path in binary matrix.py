class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        if either of the first(0, 0) or the last(n-1, n-1) element are 1 return -1
        if not do bfs starting from the first element
        in the bfs the elements to be added to the queue are the ones I can reach from the current element by going the 8 directions that I will instantiate and name DIRECTION
        the elements are added if they don't already exist in the visited set where all the elements that I have iterated over are documented
        while in the iteration if I reach the last element return with the count which is instantiated as one in the beginning and incremented by one every level
        if I don't reach the last element and I run out of cells it means I can't reach and therefore I return -1
        '''
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        dxn = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        que = deque([(0, 0, 1)])
        visited = {(0, 0)}
        
        while que:
            i, j, count = que.popleft()
            if (i, j) == (n-1, n-1):
                return count
            
            for dx in dxn:
                x, y = i+dx[0], j+dx[1]
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                    que.append((x, y, count+1))
                    visited.add((x, y))
        
        return -1
