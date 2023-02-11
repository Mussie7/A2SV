n = int(input().strip())
arr = list(map(int, input().strip().split()))

arr.sort()

if arr[-1] >= arr[-2] + arr[-3]:
    print('NO')
else:
    arr[-1], arr[-2] = arr[-2], arr[-1]
    print('YES')
    print(*arr)
