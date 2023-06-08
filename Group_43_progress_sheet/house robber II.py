class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index, first):
            if index >= len(nums):
                return 0

            if index == len(nums) - 1:
                if first:
                    return 0
                return nums[index]
            ans = max(dp(index+1, first), dp(index+2, first) + nums[index])
            return ans

        if len(nums) <= 2:
            return max(nums)

        return max(dp(0, 1), dp(1, 0))
