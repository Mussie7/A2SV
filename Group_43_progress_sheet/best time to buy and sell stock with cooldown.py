class Solution:
    # bottom-up approach
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n + 2)]
        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] - prices[i])
            dp[i][1] = max(dp[i + 1][1], dp[i + 2][0] + prices[i])

        return dp[0][0]

    # top_down approach
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(index, bought):
            if index >= n:
                return 0
            
            if not bought:
                return max(dp(index + 1, True) - prices[index], dp(index + 1, False))
            return max(dp(index + 2, False) + prices[index], dp(index + 1, True))

        n = len(prices)
        return dp(0, False)
