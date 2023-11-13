class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxVal = 1
        maxSum -= n
        grow = 1
        left = index - 1
        right = index + 1
        while (left >= 0 or right < n) and maxSum >= grow:
            maxVal += 1
            maxSum -= grow
            if left >= 0:
                grow += 1
                left -= 1
            
            if right < n:
                grow += 1
                right += 1
                
        maxVal += maxSum // grow
        return maxVal