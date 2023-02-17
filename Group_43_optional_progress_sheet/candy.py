class Solution:
    def iterate(self, start, end, jump, candies, ratings):
        for i in range(start, end, jump):
            if ratings[i] > ratings[i-jump]:
                candies[i] = max(candies[i], candies[i-jump]+1)

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        self.iterate(1, n, 1, candies, ratings)
        self.iterate(n-2, -1, -1, candies, ratings)

        return sum(candies)
