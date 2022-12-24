from collections import defaultdict

n, m = tuple(map(int, input().split()))

groupA = defaultdict(list)
for i in range(n):
    groupA[input()].append(str(i+1))

for j in range(m):
    word = input()
    if groupA[word]:
        print(' '.join(groupA[word]))
    else:
        print(-1)
