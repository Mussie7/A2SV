class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (node1, node2) in enumerate(edges):
            graph[node1].append([node2, succProb[i]])
            graph[node2].append([node1, succProb[i]])
        
        heap = [(-1, start_node)]
        prob_map = {start_node: 1}
        while heap:
            curr_prob, curr_node = heapq.heappop(heap)
            curr_prob *= -1
            for neigh, prob in graph[curr_node]:
                if neigh not in prob_map or curr_prob * prob > prob_map[neigh]:
                    prob_map[neigh] = curr_prob * prob
                    heapq.heappush(heap, (-prob_map[neigh], neigh))

        # # alternate implementation with almost equal time
        # prob_map = {}
        # while heap:
        #     curr_prob, curr_node = heapq.heappop(heap)
        #     curr_prob *= -1

        #     if curr_node in prob_map:
        #         continue            
        #     prob_map[curr_node] = curr_prob
            
        #     for neigh, prob in graph[curr_node]:
        #         if neigh not in prob_map:
        #             heapq.heappush(heap, (-(curr_prob * prob), neigh))
        
        
        if end_node not in prob_map:
            return 0.0
        return prob_map[end_node]
