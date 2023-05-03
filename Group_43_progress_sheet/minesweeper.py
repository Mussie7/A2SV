class Solution:
    def in_bound(self, i, j):
        return 0 <= i < len(self.board) and 0 <= j < len(self.board[0])

    def dfs(self, i, j):
        adj_cells = []
        bombs = 0
        for x, y in self.DIRECTION:
            x += i
            y += j
            if self.in_bound(x, y):
                if self.board[x][y] == 'E':
                    adj_cells.append((x, y))
                elif self.board[x][y] == 'M':
                    bombs += 1
        
        if bombs:
            self.board[i][j] = str(bombs)
            return
        
        self.board[i][j] = 'B'
        for r, c in adj_cells:
            self.dfs(r, c)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        elif board[r][c] == 'E':
            self.board = board
            self.DIRECTION = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            self.dfs(r, c)
        
        return board
