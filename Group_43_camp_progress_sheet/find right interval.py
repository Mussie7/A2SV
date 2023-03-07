class Solution:
    # binary search solution
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indexArray = [i for i in range(len(intervals))]
        indexArray.sort(key=lambda x:intervals[x][0])
        
        right_interval = []
        for i, (start, end) in enumerate(intervals):
            left, right = -1, len(intervals)
            while left + 1 < right:
                mid = left + (right-left) // 2
                if intervals[indexArray[mid]][0] >= end:
                    right = mid
                else:
                    left = mid
            
            if right < len(intervals):
                right_interval.append(indexArray[right])
            else:
                right_interval.append(-1)
        
        return right_interval
