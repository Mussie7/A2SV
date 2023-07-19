class Solution:
    # bottom-up approach
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(dict)
        longest = 1
        for num in nums:
            # iterate through every possible difference
            for i in range(-500, 501):
                if num - i in dp and i in dp[num - i]:
                    dp[num][i] = dp[num-i][i] + 1
                    longest = max(dp[num][i], longest)
                else:
                    dp[num][i] = 1
        
        return longest
