class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        for i in range(n-1):
            heap.append([arr[i]/arr[n-1], i, n-1])
        
        kth_smallest = [-1, -1]
        while k > 0:
            _, i, j = heapq.heappop(heap)
            kth_smallest = [arr[i], arr[j]]
            if i < j - 1:
                heapq.heappush(heap, [arr[i]/arr[j-1], i, j-1])
            
            k -= 1
        
        return kth_smallest