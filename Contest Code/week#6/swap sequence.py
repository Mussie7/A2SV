def findMax(arr, start, end):
    curmax = [arr[start], start]
    for i in range(start+1, end+1):
        if arr[i] > curmax[0]:
            curmax[0] = arr[i]
            curmax[1] = i
    
    return curmax
    
n = int(input())
arr = list(map(int, input().strip().split()))
swaps = []

for i in range(n-1, -1, -1):
    curmax = findMax(arr, 0, i)
    arr[i], arr[curmax[1]] = arr[curmax[1]], arr[i]
    swaps.append([curmax[1], i])
    
    if arr == sorted(arr): break

print(len(swaps))
for i in range(len(swaps)):
    print(*swaps[i])
