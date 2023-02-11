rep = int(input())
for _ in range(rep):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    new_arr = []
    
    i = 0
    for i in range(n//2):
        new_arr.append(arr[i])
        new_arr.append(arr[n-1-i])
    
    if n % 2:
        if i+1 < n:
            new_arr.append(arr[i+1])
        else:
            new_arr.append(arr[i])
    
    print(*new_arr)
