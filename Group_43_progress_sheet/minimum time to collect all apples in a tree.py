class Solution:
    def dfs(self, node, parent):
        time = 0
        for child in self.graph[node]:
            if child != parent:
                time += self.dfs(child, node)
        
        if node != 0 and (time or self.hasApple[node]):
            time += 2
            
        return time

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple
        self.graph = defaultdict(list)
        for parent, child in edges:
            self.graph[parent].append(child)
            self.graph[child].append(parent)
        
        return self.dfs(0, -1)
