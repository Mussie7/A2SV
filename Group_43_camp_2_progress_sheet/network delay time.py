class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node, neigh, time in times:
            graph[node].append((neigh, time))
        
        heap = [(0, k)]
        visited = set()
        maximum = 0
        while heap:
            curr_time, node = heapq.heappop(heap)
            if node in visited:
                continue
                
            maximum = max(maximum, curr_time)
            visited.add(node)
            for neigh, time in graph[node]:
                if neigh not in visited:
                    heapq.heappush(heap, (time + curr_time, neigh))
        
        if len(visited) < n:
            return -1
        return maximum
