class DetectSquares:

    def __init__(self):
        self.rows = defaultdict(list)
        self.cols = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.rows[x].append(y)
        self.cols[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        squares_count = 0
        for j in self.rows[x]:
            if j != y:
                side = abs(y - j)
                left = x - side
                right = x + side
                squares_count += self.cols[y][left] * self.cols[j][left]
                squares_count += self.cols[y][right] * self.cols[j][right]
        
        return squares_count




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)