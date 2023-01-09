class DataStream:

    def __init__(self, value: int, k: int):
        self.VALUE = value
        self.K = k
        self.count = 0

    def consec(self, num: int) -> bool:
        if num == self.VALUE:
            self.count += 1
        else:
            self.count = 0
        
        return self.count >= self.K


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
