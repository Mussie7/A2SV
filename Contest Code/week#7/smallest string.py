rep = int(input())
for _ in range(rep):
    n, m, k = map(int, input().split())
    str1 = list(input())
    str2 = list(input())
    
    str1.sort()
    str2.sort()
    
    counter1 = counter2 = 0
    pointer1 = pointer2 = 0
    new_str = []

    while pointer1 < n and pointer2 < m:
        if (str1[pointer1] < str2[pointer2] or counter2 >= k) and counter1 < k:
            new_str.append(str1[pointer1])
            pointer1 += 1
            counter1 += 1
            counter2 = 0
        else:
            new_str.append(str2[pointer2])
            pointer2 += 1
            counter2 += 1
            counter1 = 0
    
    print(''.join(new_str))
