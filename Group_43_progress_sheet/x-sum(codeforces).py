from collections import defaultdict

def bishopAttack(m, n, board):
    majorDiagonal = defaultdict(int)
    minorDiagonal = defaultdict(int)
    
    # gets the diagonal sum of the attacks
    for i in range(m):
        for j in range(n):
            majorDiagonal[i+j] += board[i][j]
            minorDiagonal[i-j] += board[i][j]
    
    maximum_damage = 0
    
    for i in range(m):
        for j in range(n):
            attack = majorDiagonal[i+j] + minorDiagonal[i-j] - board[i][j]
            maximum_damage = max(maximum_damage, attack)
    
    return maximum_damage

rep = int(input())
for _ in range(rep):
    m, n = map(int, input().split())
    
    board = []
    for _ in range(m):
        board.append(list(map(int, input().split())))
    
    print(bishopAttack(m, n, board))
