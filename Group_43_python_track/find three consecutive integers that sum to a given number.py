class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num // 3) * 3 != num:
            return
        
        smallest = (num-3) // 3
        return [smallest, smallest + 1, smallest + 2]
