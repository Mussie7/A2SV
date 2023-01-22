class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = 0

        for i in range(len(piles)-2, len(piles)//3 - 1, -2):
            coins += piles[i]
        
        return coins
