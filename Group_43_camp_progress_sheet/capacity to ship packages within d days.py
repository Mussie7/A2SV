class Solution:
    def checkCapacity(self, capacity):
        day_counter = 1
        curWeight = 0
        for i in range(len(self.weights)):
            curWeight += self.weights[i]
            if curWeight > capacity:
                curWeight = self.weights[i]
                day_counter += 1

        return day_counter <= self.days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        self.days = days

        totalLoad = sum(self.weights)
        start = max(max(self.weights), totalLoad//days)
        end = min(totalLoad, totalLoad//days + start)

        while start < end:
            mid = start + (end-start) // 2
            if self.checkCapacity(mid):
                end = mid
            else:
                start = mid + 1

        return end
