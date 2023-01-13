class Solution:
    def row_col_checker(self, board):
        for row in board:
            high_count = Counter(row).most_common(2)
            if len(high_count) == 1:
                if high_count[0][0] != '.':
                    return
                else:
                    continue

            if high_count[0][0] == '.' and high_count[1][1] > 1:
                return
            elif high_count[0][0] != '.' and high_count[0][1] > 1:
                return
        
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        if not self.row_col_checker(board) or not self.row_col_checker(list(zip(*board))):
            return
        
        quadrant = beginning = 0
        cube = set()
        while quadrant < 9:
            quadrant += 3
            for i in range(n):
                if i % 3 == 0:
                    cube = set()
                
                for j in range(beginning, quadrant):
                    print(i, j)
                    if board[i][j] != '.' and board[i][j] in cube:
                        return
                    cube.add(board[i][j])
            
            beginning += 3
        
        return True
