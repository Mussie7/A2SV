rep = int(input())
for _ in range(rep):
    n, m = (map(int, input().split()))
    
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    
    for i in range(n-2, -1, -1):
        for j in range(m):
            if grid[i][j] == '*':
                row = i+1
                while row < n and grid[row][j] == '.':
                    row += 1
                
                grid[i][j], grid[row-1][j] = grid[row-1][j], grid[i][j]
    
    for i in range(n):
        print(''.join(grid[i]))
