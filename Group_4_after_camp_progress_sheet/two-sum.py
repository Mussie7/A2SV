class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for i, num in enumerate(nums):
            if target - num in prev_nums:
                return prev_nums[target - num], i
            
            prev_nums[num] = i