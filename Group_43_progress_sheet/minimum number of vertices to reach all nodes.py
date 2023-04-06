class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = {i for i in range(n)}
        for i, o in edges:
            if o in nodes:
                nodes.remove(o)
        
        return nodes
