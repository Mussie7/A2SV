rep = int(input().strip())
for _ in range(rep):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    
    arr.sort()
    impossible = False
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] > 1:
            impossible = True
            break
    
    if impossible:
        print('NO')
    else:
        print('YES')
