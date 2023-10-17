class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_power = math.ceil(n / 2)
        prime_power = n - even_power
        mod = 10**9 + 7
        return pow(pow(5, even_power, mod) * pow(4, prime_power, mod), 1, mod)
