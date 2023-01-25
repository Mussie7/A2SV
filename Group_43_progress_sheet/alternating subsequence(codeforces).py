rep = int(input().strip())
for _ in range(rep):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    
    sign = arr[0] // abs(arr[0])
    cur_element = arr[0]
    max_sum = 0
    
    for i in range(n):
        if arr[i] // abs(arr[i]) != sign:
            max_sum += cur_element
            cur_element = arr[i]
            sign = -sign
        else:
            cur_element = max(cur_element, arr[i])
    
    max_sum += cur_element
    print(max_sum)
