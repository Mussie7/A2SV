rep = int(input())
for _ in range(rep):
    n, k = (map(int, input().split()))
    arr = list(map(int, input().strip().split()))
    
    found = False
    arr_set = set(arr)
    
    for i in range(n):
        if arr[i]-k in arr_set or arr[i]+k in arr_set:
            found = True
            break
    
    if found:
        print('yEs')
    else:
        print('nO')
