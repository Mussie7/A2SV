class Solution:
    def dfs(self, parent, node, labels, graph, sameLabelSubtree):
        charArray = Counter()
        for edge in graph[node]:
            if edge != parent:
                charArray += self.dfs(node, edge, labels, graph, sameLabelSubtree)

        charArray[labels[node]] += 1    
        sameLabelSubtree[node] = charArray[labels[node]]
        return charArray
        
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for node, edge in edges:
            graph[node].append(edge)
            graph[edge].append(node)

        sameLabelSubtree = [0] * n
        self.dfs(-1, 0, labels, graph, sameLabelSubtree)
        return sameLabelSubtree
    
    
    
# better code
class Solution:
    def dfs(self, parent, node):
        prev = self.label_counter[self.labels[node]]
        self.label_counter[self.labels[node]] += 1
        for edge in self.graph[node]:
            if edge != parent:
                self.dfs(node, edge)

        self.sameLabelSubtree[node] = self.label_counter[self.labels[node]] - prev
        
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.labels = labels
        self.graph = defaultdict(list)
        for node, edge in edges:
            self.graph[node].append(edge)
            self.graph[edge].append(node)

        self.label_counter = Counter()
        self.sameLabelSubtree = [0] * n
        self.dfs(-1, 0)
        return self.sameLabelSubtree
