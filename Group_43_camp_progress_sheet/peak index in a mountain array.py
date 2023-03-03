class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = left + (right-left) // 2
            if arr[mid] - arr[mid-1] > 0:
                left = mid
            else:
                right = mid
        
        return left
