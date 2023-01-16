rep = int(input())

for _ in range(rep):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(input())
    
    whole_count = 0
    for i in range(n//2):
        for j in range(i, n-1-i):
            count = [0, 0]
            count[int(board[i][j])] += 1
            count[int(board[j][n-1-i])] += 1
            count[int(board[n-1-i][n-1-j])] += 1
            count[int(board[n-1-j][i])] += 1
            
            whole_count += min(count)
    
    print(whole_count)
