n = int(input())
count_roads = 0
for _ in range(n):
    count_roads += list(map(int, input().strip().split())).count(1)

print(count_roads // 2)
