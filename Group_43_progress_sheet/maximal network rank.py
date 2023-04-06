class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
        
        max_network_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                network_rank = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    network_rank -= 1
                max_network_rank = max(max_network_rank, network_rank)
        
        return max_network_rank
