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

# faster, cooler solution
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles_count = defaultdict(int)
        max_pile = piles_total = 0
        for pile in piles:
            max_pile = max(pile, max_pile)
            piles_total += pile
            piles_count[pile] += 1
        
        pile = max_pile
        while k:
            if piles_count[pile] > 0:
                piles_count[pile] -= 1
                k -= 1
                amount = pile // 2
                piles_total -= amount
                piles_count[pile - amount] += 1
            else:
                pile -= 1

        return piles_total
