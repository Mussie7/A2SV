# top-down approach
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(curr, index):
            if index >= len(nums):
                return int(curr == target)
            
            return dp(curr + nums[index], index + 1) + dp(curr - nums[index], index + 1)
        
        return dp(0, 0)
