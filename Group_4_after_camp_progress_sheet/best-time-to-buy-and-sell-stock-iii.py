class Solution:
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