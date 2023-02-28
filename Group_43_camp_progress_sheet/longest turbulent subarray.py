class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        parity = 0
        maxLen = 1
        for right in range(1, len(arr)):
            if arr[right] == arr[right-1]:
                parity = 0
                left = right
                continue
            
            if (arr[right] - arr[right-1]) // abs(arr[right] - arr[right-1]) == parity:
                left = right - 1
            else:
                parity = (arr[right] - arr[right-1]) // abs(arr[right] - arr[right-1])
            
            maxLen = max(maxLen, right-left+1)
        
        return maxLen
