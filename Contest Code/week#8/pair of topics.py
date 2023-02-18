n = int(input())
teachers = list(map(int, input().split()))
students = list(map(int, input().split()))

diff = []
for i in range(n):
    diff.append(teachers[i] - students[i])

diff.sort()
topics = 0
left = 0
for i in range(n-1, -1, -1):
    while left < i and diff[i] + diff[left] <= 0:
        left += 1
    
    if left >= i:
        break
    
    topics += i - left

print(topics)
