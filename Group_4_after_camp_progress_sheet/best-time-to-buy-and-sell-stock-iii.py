class Solution:
    # top-down approach
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(index, buy, remaining):
            if index == n or remaining == 0:
                return 0
            
            if buy:
                return max(dp(index + 1, not buy, remaining) - prices[index], dp(index + 1, buy, remaining))
            return max(dp(index + 1, not buy, remaining - 1) + prices[index], dp(index + 1, buy, remaining))
        
        n = len(prices)
        return dp(0, True, 2)


    # bottom-up approach
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0, 0, 0] for _ in range(2)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(2):
                for k in [2, 1]:
                    if j == 0:
                        dp[i][j][k] = max(dp[i + 1][1 - j][k] - prices[i], dp[i + 1][j][k])
                    else:
                        dp[i][j][k] = max(dp[i + 1][1- j][k - 1] + prices[i], dp[i + 1][j][k])

        return dp[0][0][2]
