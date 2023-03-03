class StockSpanner:

    def __init__(self):
        self.decStack = []

    def next(self, price: int) -> int:
        days = 1
        while self.decStack and price >= self.decStack[-1][0]:
            days += self.decStack.pop()[1]
        
        self.decStack.append([price, days])
        return self.decStack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
