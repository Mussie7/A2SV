n, m, k = map(int, input().split())
mat = []

for _ in range(n):
    mat.append(input())

arrange = 0

for row in mat:
    count = 0
    for seat in row:
        if seat == '.':
            count += 1
            if count >= k:
                arrange += 1
        else:
            count = 0
if k > 1:
    for col in range(m):
        count = 0
        for row in range(n):
            if mat[row][col] == '.':
                count += 1
                if count >= k:
                    arrange += 1
            else:
                count = 0

print(arrange)
