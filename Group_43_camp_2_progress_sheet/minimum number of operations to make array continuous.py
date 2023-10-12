class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        operations = n
        for i in range(len(nums)):
            idx = bisect.bisect_left(nums, nums[i] + n)
            operations = min(operations, i + len(nums) - idx)
        
        return operations + n - len(nums)
