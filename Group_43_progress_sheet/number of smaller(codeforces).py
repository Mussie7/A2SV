n, m = (map(int, input().split()))
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))
pointer = 0
arr = []

for i in range(m):
    while pointer < n and n_arr[pointer] < m_arr[i]:
        pointer += 1
    
    arr.append(pointer)

print(*arr)
