from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))

counter = Counter()
for _ in range(m):
    counter[input()] += 1

toys = list(counter.values())
toys.sort(reverse=True)
arr.sort()

minCost = maxCost = 0
for i in range(len(toys)):
    minCost += toys[i] * arr[i]
    maxCost += toys[i] * arr[n-i-1]

print(minCost, maxCost)
