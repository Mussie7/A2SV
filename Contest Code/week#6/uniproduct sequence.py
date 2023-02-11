n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort()

neg = 0
coins = 0
for num in arr:
    if num < 0:
        coins += -1 - num
        neg += 1
    elif num >= 0 and neg % 2:
        coins += num + 1
        neg += 1
    else:
        coins += abs(num - 1)

if neg % 2:
    coins += 2

print(coins)
