class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cons_sub = defaultdict(list)
        for num in nums:
            count = 1
            if cons_sub[num-1]:
                count += heapq.heappop(cons_sub[num-1])
            heapq.heappush(cons_sub[num], count)
        
        for heap in cons_sub.values():
            if heap and heap[0] < 3:
                return False
        
        return True
