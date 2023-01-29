rep = int(input().strip())
for _ in range(rep):
    n, k = (map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    
    count, subarray = 0, 1
    for i in range(1, n):
        if arr[i] * 2 > arr[i-1]:
            subarray += 1
        else:
            subarray = 1
        
        if subarray > k:
            count += 1
    
    print(count)
