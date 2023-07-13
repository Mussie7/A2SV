class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            curr_diff = heights[i+1] - heights[i]
            if curr_diff > 0:
                heapq.heappush(heap, -curr_diff)
                bricks -= curr_diff

                if bricks < 0 and ladders > 0:
                    bricks -= heapq.heappop(heap)
                    ladders -= 1
                elif bricks < 0 and ladders == 0:
                    return i
        
        return len(heights) - 1
