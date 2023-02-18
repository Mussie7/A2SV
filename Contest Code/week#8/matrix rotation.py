rep = int(input())
for _ in range(rep):
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    
    min_element = min(min(row1), min(row2))
    max_element = max(max(row1), max(row2))
    
    if min_element in row1 and max_element in row1:
        print('NO')
    elif min_element in row2 and max_element in row2:
        print('NO')
    elif (row1[0] == min_element and row2[0] == max_element) or (row1[0] == max_element and row2[0] == min_element) or (row1[1] == max_element and row2[1] == min_element) or (row2[1] == max_element and row1[1] == min_element):
        print('NO')
    else:
        print('YES')
