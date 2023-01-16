from collections import Counter
rep = int(input())
for _ in range(rep):
    rect1 = list(map(int, input().split()))
    rect2 = list(map(int, input().split()))
    
    if max(rect1) != max(rect2):
        print('NO')
    elif max(rect1) != min(rect1) + min(rect2):
        print('NO')
    else:
        print('YES')
