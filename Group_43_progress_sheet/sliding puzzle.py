class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        in_bound = lambda i, j : 0 <= i < len(board) and 0 <= j < len(board[0])

        def find_zero(b):
            for i in range(len(b)):
                for j in range(len(b[0])):
                    if b[i][j] == 0:
                        return (i, j)

        def make_board(b, num):
            new_b = []
            for i in range(len(b)):
                new_b.append([])
                for j in range(len(b[0])):
                    if b[i][j] == 0:
                        new_b[i].append(num)
                    elif b[i][j] == num:
                        new_b[i].append(0)
                    else:
                        new_b[i].append(b[i][j])
                
                new_b[i] = tuple(new_b[i])
            
            return tuple(new_b)


        board[0] = tuple(board[0])
        board[1] = tuple(board[1])
        board = tuple(board)
        que = deque([(board, 0)])
        visited = {board}
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while que:
            board, move = que.popleft()
            if board == ((1, 2, 3), (4, 5, 0)):
                return move
            
            i, j = find_zero(board)
            for x, y in DIRECTIONS:
                x += i
                y += j
                if in_bound(x, y):
                    new_board = make_board(board, board[x][y])
                    if new_board not in visited:
                        que.append((new_board, move + 1))
                        visited.add(new_board)
        
        return -1
