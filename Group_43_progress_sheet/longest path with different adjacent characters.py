class Solution:
    def dfs(self, node):
        curr_len = 1
        for child in self.graph[node]:
            child_len = self.dfs(child)
            if self.s[node] != self.s[child]:
                self.max_len = max(self.max_len, curr_len + child_len)
                curr_len = max(curr_len, child_len + 1)
        
        return curr_len

    def longestPath(self, parent: List[int], s: str) -> int:
        self.s = s
        self.graph = defaultdict(list)
        for i in range(1, len(parent)):
            self.graph[parent[i]].append(i)
        
        self.max_len = 1
        self.dfs(0)
        return self.max_len
