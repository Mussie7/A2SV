class Solution:
    def countOrders(self, n: int) -> int:
        return pow(math.factorial(2 * n) // 2 ** n, 1, 10 ** 9 + 7)
