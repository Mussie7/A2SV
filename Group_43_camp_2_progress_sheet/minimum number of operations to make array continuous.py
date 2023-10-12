class Solution:
    # binary search implementation
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        operations = n
        for i in range(len(nums)):
            idx = bisect.bisect_left(nums, nums[i] + n)
            operations = min(operations, i + len(nums) - idx)
        
        return operations + n - len(nums)

    # sliding window implementation
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        operations = n
        right = 0
        for left in range(len(nums)):
            end = nums[left] + n - 1
            while right < len(nums) and nums[right] <= end:
                right += 1
            
            operations = min(operations, left + len(nums) - right)
            if right == n:
                break
        
        return operations + n - len(nums)
