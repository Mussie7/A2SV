class Solution:
    def factorize(self, num):
        prime = 2
        while prime * prime <= num:
            while num % prime == 0:
                self.primeFactors.add(prime)
                num //= prime
            prime += 1
        
        if num > 1:
            self.primeFactors.add(num)

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        self.primeFactors = set()
        for num in nums:
            self.factorize(num)
        
        return len(self.primeFactors)
