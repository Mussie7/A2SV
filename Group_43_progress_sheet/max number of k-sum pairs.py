class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        operations = 0

        while left < right:
            curSum = nums[left] + nums[right]
            if curSum == k:
                left += 1
                right -= 1
                operations += 1
            elif curSum > k:
                right -= 1
            else:
                left += 1
        
        return operations
