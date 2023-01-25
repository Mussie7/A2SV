class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(math.floor(math.sqrt(c))+1):
            other = math.sqrt(c - i**2)
            if other == int(other):
                return True
              
# two pointer solution
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            current = left**2 + right**2
            if current == c:
                return True
            elif current > c:
                right -= 1
            else:
                left += 1
