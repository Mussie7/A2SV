class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        miles = [0] * 1001
        for passangers, start, end in trips:
            miles[start] += passangers
            miles[end] -= passangers

        if miles[0] > capacity:
            return
        
        for mile in range(1, len(miles)):
            miles[mile] += miles[mile-1]
            if miles[mile] > capacity:
                return
        
        return True
