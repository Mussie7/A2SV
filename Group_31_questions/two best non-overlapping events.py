class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        best = 0
        start = sorted(events, key=lambda events:events[0])
        value = [0] * (len(start) + 1)
        for i in range(len(start) - 1, -1, -1):
            value[i] = max(start[i][2], value[i+1])
        end = sorted(events, key=lambda events:events[1])
        
        e = 0
        for j in range(len(end)):
            while e < len(start) and end[j][1] >= start[e][0]:
                e += 1
            best = max(best, end[j][2]+value[e])
        
        return best
