class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        # instantiate the edge count array by setting the count of edges to every node to zero
        edge_count = {i: 0 for i in range(n)}
        for node, neigh in edges:
            graph[node].append(neigh)
            graph[neigh].append(node)
            
            edge_count[node] += 1
            edge_count[neigh] += 1
           
        que = deque()
        visited = set()
        # add all the leaf nodes to your queue
        for node in edge_count:
            if edge_count[node] <= 1:
                que.append(node)
                visited.add(node)
        
        components_count = 0
        while que:
            node = que.popleft()
            # for every leaf node find its parent
            for neigh in graph[node]:
                edge_count[neigh] -= 1
                if neigh not in visited: 
                    parent = neigh
                    # if all it's leaf nodes have been visited the node becomes a leaf node and so add it to your que
                    if edge_count[neigh] <= 1:
                        visited.add(parent)
                        que.append(parent)

            # if the current leaf node can be a component add it as a component and if it can add it's value to it's parent
            if values[node] % k == 0:
                components_count += 1
            else:
                values[parent] += values[node]
        
        return components_count
