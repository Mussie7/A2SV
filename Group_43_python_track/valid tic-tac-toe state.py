class Solution:
    def help(self, board):
        total_x = total_o = 0
        left_diagonal, right_diagonal = [0] * 3, [0] * 3
        complete = [False, '']

        i = 0
        for row in board:
            left_diagonal[i] = row[i]
            right_diagonal[i] = row[-i-1]
            count_x = row.count('X')
            count_o = row.count('O')

            if complete[0] and (count_x == 3 or count_o == 3): return
            elif count_x == 3:
                complete[0] = True
                complete[1] = 'X'
            elif count_o == 3:
                complete[0] = True
                complete[1] = 'O'
            
            i += 1
            total_x += count_x
            total_o += count_o

        if left_diagonal.count('X') == 3 or right_diagonal.count('X') == 3:
            complete[0] = True
            complete[1] = 'X'
        elif left_diagonal.count('O') == 3 or right_diagonal.count('O') == 3:
            complete[0] = True
            complete[1] = 'O'

        return (complete, total_x, total_o)
        
    def validTicTacToe(self, board: List[str]) -> bool:
        for _ in range(2):
            tupl = self.help(board)
            if not tupl: return
            
            complete, total_x, total_o = tupl
            if total_x - total_o > 1 or total_o > total_x: return
            elif complete[0] and complete[1] == 'X' and total_x == total_o: return
            elif complete[0] and complete[1] == 'O' and total_x > total_o: return
            
            new_board = []
            for column in zip(*board):
                new_board.append(column)
            
            board = new_board

        return True
