class Solution: 
    def select(self, arr, i):
        curMin = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < curMin:
                curMin = arr[j]
        
        return curMin
    
    def selectionSort(self, arr,n):
        for i in range(n):
            j = i + arr[i:].index(self.select(arr, i))
            arr[i], arr[j] = arr[j], arr[i]

        return arr
