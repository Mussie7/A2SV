from collections import Counter, defaultdict

def crossRow(grid, m):
    row_dic = defaultdict(list)
    for i in range(m):
        for letter, count in Counter(grid[i]).most_common():
            if count == 1:
                break
            row_dic[i].append(letter)
    
    return row_dic

def crossColumn(grid):
    col_dic = defaultdict(list)
    i = 0
    for col in zip(*grid):
        for letter, count in Counter(col).most_common():
            if count == 1:
                break
            col_dic[i].append(letter)
        i += 1
    
    return col_dic

m, n = (map(int, input().strip().split()))
grid = []

for _ in range(m):
    grid.append(list(input().strip()))

row_dic = crossRow(grid, m)
col_dic = crossColumn(grid)

for index, letters in row_dic.items():
    for letter in letters:
        for j in range(n):
            if grid[index][j] == letter:
                grid[index][j] = ''

for index, letters in col_dic.items():
    for letter in letters:
        for i in range(m):
            if grid[i][index] == letter:
                grid[i][index] = ''

solve = []
for row in grid:
    solve.append(''.join(row))

print(''.join(solve))
