class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = -1, n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if n - mid <= citations[mid]:
                right = mid
            else:
                left = mid
        
        return n - right
