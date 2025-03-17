def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        prev = swaps
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
        
        if prev == swaps:
            break
    print('Array is sorted in ' + str(swaps) + ' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[-1]))
