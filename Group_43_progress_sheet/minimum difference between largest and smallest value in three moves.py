class Solution:
    def minDifference(self, nums: List[int]) -> int:
        def dp(nums, depth):
            if not nums:
                return 0
            if depth == 3:
                return nums[-1] - nums[0]
            
            return min(dp(nums[:-1], depth + 1), dp(nums[1:], depth + 1))

        nums.sort()
        return dp(nums, 0)
