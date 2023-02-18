n = int(input())
arr = list(map(int, input().split()))

count = 1
subsegment = 1
for i in range(1, n):
    if arr[i] < arr[i-1]:
        subsegment = max(count, subsegment)
        count = 0
    
    count += 1
subsegment = max(subsegment, count)

print(subsegment)
