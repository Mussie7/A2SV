# bfs topological sort implementation
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        graph = defaultdict(list)
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

            in_degree[parent] += 1
            in_degree[child] += 1
        
        que = deque([])
        for node in range(n):
            if in_degree[node] <= 1:
                que.append(node)
        
        non_roots = 0
        while que:
            if len(que) + non_roots == n:
                return que
            
            non_roots += len(que)
            for _ in range(len(que)):
                node = que.popleft()
                for parent in graph[node]:
                    in_degree[parent] -= 1
                    if in_degree[parent] == 1:
                        que.append(parent)            
