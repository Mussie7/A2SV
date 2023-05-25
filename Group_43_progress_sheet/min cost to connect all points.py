class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        
        # path compression
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        if rep1 == rep2:
            return False

        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]
        
        return True

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        possibilities = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                man_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                possibilities.append([man_dist, points[i], points[j]])
        possibilities.sort()
        
        self.rep = {}
        self.rank = {}
        min_cost, connections = 0, len(points) - 1
        for cost, point1, point2 in possibilities:
            point1, point2 = tuple(point1), tuple(point2)
            if point1 not in self.rep:
                self.rep[point1] = point1
                self.rank[point1] = 1
            
            if point2 not in self.rep:
                self.rep[point2] = point2
                self.rank[point2] = 1
            
            if self.union(point1, point2):
                min_cost += cost
                connections -= 1
            
            if not connections:
                return min_cost
        return 0
