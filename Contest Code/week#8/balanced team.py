n = int(input())
arr = list(map(int, input().split()))

arr.sort()
left, right = 0, 1
team = 1

for right in range(1, n):
    while left < right and arr[right] - arr[left] > 5:
        left += 1
    
    team = max(team, right - left + 1)

print(team)
