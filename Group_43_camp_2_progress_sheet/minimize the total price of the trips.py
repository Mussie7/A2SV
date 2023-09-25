class Solution:
    # a function to find the path for the trips
    def pathFinder(self, start: int, end: int) -> list:
        def dfs(node, parent):
            # return when you reach the destination
            if node == end:
                return [end]
            
            for neigh in self.graph[node]:
                if neigh != parent:
                    path = dfs(neigh, node)
                    if path:
                        path.append(node)
                        return path
        
        return dfs(start, -1)

    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        @cache
        def dp(node, parent, adjacent):
            # if the current node is not halved
            curr_price = price[node] * node_counter[node]
            for neigh in self.graph[node]:
                if neigh != parent:
                    curr_price += dp(neigh, node, False)
            
            alternate_price = inf
            # if this node is not adjacent to a halved node you have to check the possiblity of halving this node
            if adjacent == False:
                alternate_price = (price[node] // 2) * node_counter[node]
                for neigh in self.graph[node]:
                    if neigh != parent:
                        # mark the neighbouring nodes as adjacent to a halved node
                        alternate_price += dp(neigh, node, True)
            
            return min(curr_price, alternate_price)
            
        # graph construction
        self.graph = defaultdict(list)
        for node, neigh in edges:
            self.graph[node].append(neigh)
            self.graph[neigh].append(node)

        node_counter = Counter()
        for start, end in trips:
            # count the number of mentions of every node in every trip
            node_counter += Counter(self.pathFinder(start, end))
        
        return dp(0, -1, False)
