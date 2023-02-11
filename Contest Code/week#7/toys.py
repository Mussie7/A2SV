from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))

counter = Counter()
for _ in range(m):
    counter[input()] += 1

toys = list(counter.values())

toys.sort()
arr.sort()

toyPointer = len(toys)-1
minCost = maxCost = 0
for i in range(n):
    if toyPointer < 0:
        break
    
    minCost += toys[toyPointer] * arr[i]
    maxCost += toys[toyPointer] * arr[n-i-1]
    toyPointer -= 1

print(minCost, maxCost)
