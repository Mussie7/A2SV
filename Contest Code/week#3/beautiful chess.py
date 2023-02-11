from collections import Counter
rep = int(input())
for _ in range(rep):
    input()
    board = []
    for _ in range(8):
        board.append(input().strip())
    
    finder = []
    for i in range(8):
        finder.append(Counter(board[i])['#'])
    
    for i in range(1, 7):
        if finder[i] == 1:
            if finder[i-1] == 2 and finder[i+1] == 2:
                row = i
                break
    
    for j in range(8):
        if board[row][j] == '#':
            print(row+1, j+1)
            break
