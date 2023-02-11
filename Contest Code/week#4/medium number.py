rep = int(input())
for _ in range(rep):
    arr = list(map(int, input().strip().split()))
    arr.sort()
    print(arr[1])
