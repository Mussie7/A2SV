class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return 
        
        if arr[0] > arr[1] or arr[-1] > arr[-2]:
            return
        
        upslope = True
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return

            if upslope and arr[i] < arr[i-1]:
                upslope = False
            
            if not upslope and arr[i] > arr[i-1]:
                return
        
        return True
