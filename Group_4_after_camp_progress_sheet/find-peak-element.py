class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == n - 1 or nums[mid] > nums[mid + 1]):
                return mid
            
            elif nums[mid + 1] > nums[mid]:
                left = mid
            else:
                right = mid