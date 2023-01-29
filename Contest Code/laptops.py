rep = int(input())
arr = []
for _ in range(rep):
    arr.append(list(map(int, input().strip().split())))

arr.sort()
found = False
for i in range(1, len(arr)):
    if arr[i][0] > arr[i-1][0]:
        if arr[i][1] < arr[i-1][1]:
            found = True
            break

if found:
    print('Happy Alex')
else:
    print('Poor Alex')
