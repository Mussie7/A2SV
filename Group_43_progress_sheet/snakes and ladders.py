class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        que = deque([(0, 0)])
        visited = {0}
        while que:
            curr, moves = que.popleft()
            if curr == target - 1:
                return moves

            for nxt in range(curr + 1, min(curr + 7, target)):
                row = nxt // n
                col = nxt % n
                if row % 2:
                    col = (n-1) - col
                row = (n-1) - row

                if nxt not in visited and board[row][col] == -1:
                    que.append((nxt, moves + 1))
                    visited.add(nxt)
                elif board[row][col] != -1 and (board[row][col] - 1) not in visited:
                    que.append((board[row][col] - 1, moves + 1))
                    visited.add(board[row][col] - 1)
        
        return -1
