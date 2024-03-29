class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y, x = heapq.heappop(heap), heapq.heappop(heap)
            if x - y or not heap:
                heapq.heappush(heap, y - x)
        
        return -heap[0]
