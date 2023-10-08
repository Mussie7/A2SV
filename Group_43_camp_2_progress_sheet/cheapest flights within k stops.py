class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for fro, to, price in flights:
            graph[fro].append([to, price])
        
        heap = [(0, src, 0, -1)]
        cheapest = -1
        visited = set()
        while heap:
            curr_price, curr_city, stop_count, parent = heapq.heappop(heap)
            if curr_city == dst:
                cheapest = curr_price
                break
            
            if (curr_city, stop_count) in visited:
                continue

            visited.add((curr_city, stop_count))            
            if stop_count > k:
                continue
            
            for city, price in graph[curr_city]:
                if (city, stop_count) not in visited:
                    heapq.heappush(heap, [curr_price + price, city, stop_count + 1, curr_city])
        
        return cheapest
