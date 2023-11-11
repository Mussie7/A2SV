class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.path = defaultdict(lambda: inf)
        for fro, to, cost in edges:
            self.path[(fro, to)] = cost
        
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if i == j:
                        self.path[(i, j)] = 0
                    self.path[(i, j)] = min(self.path[(i, j)], self.path[(i, k)] + self.path[(k, j)])
        

    def addEdge(self, edge: List[int]) -> None:
        fro, to, cost = edge
        if cost >= self.path[(fro, to)]:
            return
        
        self.path[(fro, to)] = cost
        for k in [fro, to]:
            for i in range(self.n):
                for j in range(self.n):
                    self.path[(i, j)] = min(self.path[(i, j)], self.path[(i, k)] + self.path[(k, j)])
            

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.path[(node1, node2)] if self.path[(node1, node2)] != inf else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)