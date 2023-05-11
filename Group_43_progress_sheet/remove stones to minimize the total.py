class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        
        heapq.heapify(piles)
        while k and piles[0]:
            num = heapq.heappop(piles)
            # because num is negative I don't have to call math.ceil
            heapq.heappush(piles, num // 2)
            k -= 1

        return -sum(piles)
