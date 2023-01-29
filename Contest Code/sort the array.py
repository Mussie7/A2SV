rep = int(input())
arr = list(map(int, input().strip().split()))

def check(rep, arr):
    start, end = None, None
    for i in range(1, rep):
        if not start and arr[i] < arr[i-1]:
            start = i
        if start and not end and arr[i] > arr[i-1]:
            end = i
        if start and end and arr[i] < arr[i-1]:
            return False
    
    
        
    if not start:
        return [1, 1]
    elif not end:
        end = rep
        if start > 1 and arr[end-1] < arr[start-2]:
            return False
        return [start, end]
    elif end and arr[start-1] > arr[end]:
        return False
    
    return [start, end]

ch = check(rep, arr)
if ch == False:
    print('no')
else:
    print('yes')
    print(*ch)
