class Solution:
    def checkSpeed(self, speed):
        hours = 0
        for pile in self.piles:
            hours += math.ceil(pile/speed)
        
        return hours <= self.h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        left, right = 0, max(piles) + 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.checkSpeed(mid):
                right = mid
            else:
                left = mid
        
        return right
