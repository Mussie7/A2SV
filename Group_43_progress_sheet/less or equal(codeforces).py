n, k = (map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
arr.sort()

if k == 0:
    if arr[0] == 1:
        print(-1)
    else:
        print(arr[0] - 1)
elif k < n and arr[k-1] == arr[k]:
    print(-1)
else:
    print(arr[k-1])
