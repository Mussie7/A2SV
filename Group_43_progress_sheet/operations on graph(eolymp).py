from collections import defaultdict

n = int(input().strip())
k = int(input().strip())
graph = defaultdict(list)
for _ in range(k):
    instruction = list(map(int, input().strip().split()))
    if instruction[0] == 1:
        graph[instruction[1]].append(instruction[2])
        graph[instruction[2]].append(instruction[1])
    else:
        print(*graph[instruction[1]])
