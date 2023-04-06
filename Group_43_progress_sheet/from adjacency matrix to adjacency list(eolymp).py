n  = int(input())
adj_mat = []
for _ in range(n):
    adj_mat.append(list(map(int, input().strip().split())))

adj_list = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if adj_mat[i][j] == 1:
            adj_list[i].append(j+1)

for i in range(n):
    print(len(adj_list[i]), *adj_list[i])
