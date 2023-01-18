def insertionSort1(n, arr):
    e = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > e:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = e
            print(*arr)
            break
    
        if i == 0:
            arr[i] = e
            print(*arr)
