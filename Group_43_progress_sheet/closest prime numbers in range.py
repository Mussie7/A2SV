# my solution
n = 1000000
is_prime = [True for i in range(n+1)]
is_prime[0] = is_prime[1] = False

i = 2
while i * i <= n:
    if is_prime[i]:
        j = i * i
        while j <= n:
            is_prime[j] = False
            j += i
    
    i = i + 1 if i == 2 else i + 2


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        min_distance = inf
        prev = -inf
        ans = [-1, -1]
        for num in range(left, right+1):
            if is_prime[num]:
                if num - prev < min_distance:
                    ans = [prev, num]
                    min_distance = num - prev
                prev = num
            
            if min_distance < 3:
                return ans
        
        return ans
      
      
    # Better solution (not so much in time but in formality)
    def is_prime(self, num):
        for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        min_distance = inf
        prev = -inf
        ans = [-1, -1]
        for num in range(max(2, left), right+1):
            if (num == 2 or num % 2) and self.is_prime(num):
                if num - prev < min_distance:
                    min_distance = num - prev
                    ans = [prev, num]
                prev = num
            
            if min_distance < 3:
                return ans
        
        return ans
