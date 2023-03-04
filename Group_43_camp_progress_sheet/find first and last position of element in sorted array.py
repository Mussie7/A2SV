class Solution:
    def bs(self, target, last=False):
        if last:
            target += 1

        left, right = -1, len(self.nums)
        while left + 1 < right:
            mid = left + (right-left) // 2
            if self.nums[mid] >= target:
                right = mid
            else:
                left = mid
            
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        start = self.bs(target)
        if start == len(nums) or self.nums[start] != target:
            return [-1, -1]
        
        return [start, self.bs(target, True) - 1]
