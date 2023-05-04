class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                graph[routes[i][j]].append(i)
        
        que = deque(graph[source])
        visited_buses = set(graph[source])
        visited_stops = set()
        level = 1
        while que:
            for _ in range(len(que)):
                bus = que.popleft()
                for stop in routes[bus]:
                    if stop == target:
                        return level
                    
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        for b in graph[stop]:
                            if b not in visited_buses:
                                visited_buses.add(b)
                                que.append(b)
            level += 1
        
        return -1
