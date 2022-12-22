class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis, index = inf, None
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                temp = abs(x - point[0]) + abs(y - point[1])
                if temp < dis:
                    dis = temp
                    index = i
                    
        return index if index is not None else -1
