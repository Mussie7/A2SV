class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @cache
        def dp(index, sign):
            max_subsequence = 1
            for i in range(index + 1, n):
                if (nums[i] - nums[index]) != 0 and (nums[i] - nums[index]) // abs(nums[i] - nums[index]) == -sign:
                    max_subsequence = max(max_subsequence, dp(i, -sign) + 1)
                
            return max_subsequence

        n = len(nums)
        return max(dp(0, 1), dp(0, -1))
