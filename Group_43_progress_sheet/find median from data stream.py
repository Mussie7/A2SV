class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:
        if len(self.first_half) > len(self.second_half):
            heapq.heappush(self.second_half, -heappushpop(self.first_half, -num))
        else:
            heapq.heappush(self.first_half, -heappushpop(self.second_half, num))

    def findMedian(self) -> float:
        if len(self.first_half) > len(self.second_half):
            return -self.first_half[0]
        else:
            return (self.second_half[0] - self.first_half[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
