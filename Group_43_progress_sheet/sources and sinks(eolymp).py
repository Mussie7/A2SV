n = int(input().strip())
adj_mat = []
for _ in range(n):
    adj_mat.append(list(map(int, input().strip().split())))

in_and_out = [[0, 0] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if adj_mat[i][j] == 1:
            in_and_out[i][1] += 1
            in_and_out[j][0] += 1

sink = []
source = []
for vertex, (i, o) in enumerate(in_and_out):
    if i == 0:
        source.append(vertex + 1)
    if o == 0:
        sink.append(vertex + 1)

print(len(source), *source)
print(len(sink), *sink)
