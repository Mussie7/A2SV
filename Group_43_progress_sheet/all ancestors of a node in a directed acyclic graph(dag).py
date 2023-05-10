class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]
        que = {i for i in range(n)}
        parent_count = [0] * n
        for parent, child in edges:
            graph[parent].append(child)
            que.discard(child)
            parent_count[child] += 1
        
        que = deque(que)
        while que:
            parent = que.popleft()
            for child in graph[parent]:
                ancestors[child].append(parent)
                ancestors[child].extend(ancestors[parent])
                parent_count[child] -= 1
                if parent_count[child] == 0:
                    que.append(child)
                    ancestors[child] = sorted(set(ancestors[child]))
        
        return ancestors
