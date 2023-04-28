class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        in_bound = lambda i, j: 0 <= i < m and 0 <= j < n and board[i][j] == 'O'
        def dfs(i, j):
            zeros.add((i, j))
            for x, y in DIRECTIONS:
                x += i
                y += j
                if in_bound(x, y) and (x, y) not in zeros:
                    dfs(x, y)
        
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[0])
        zeros = set()
        for j in range(0, n, max(n-1, 1)):
            for i in range(m):
                if board[i][j] == 'O':
                    if (i, j) not in zeros:
                        dfs(i, j)
        
        for i in range(0, m, max(m-1, 1)):
            for j in range(n):
                if board[i][j] == 'O':
                    if (i, j) not in zeros:
                        dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in zeros:
                    board[i][j] = 'X'
