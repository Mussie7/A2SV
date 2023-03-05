class Solution:
    def divideNums(self, divider):
        result = 0
        for num in self.nums:
            result += math.ceil(num/divider)
        
        return result <= self.threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        self.nums = nums
        self.threshold = threshold

        left, right = 0, max(nums)+1
        while left + 1 < right:
            mid = left + (right-left) // 2
            if self.divideNums(mid):
                right = mid
            else:
                left = mid
        
        return right
