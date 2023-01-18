def countingSort(arr):
    counter_arr = [0] * 100
    for num in arr:
        counter_arr[num] += 1
    
    return counter_arr
