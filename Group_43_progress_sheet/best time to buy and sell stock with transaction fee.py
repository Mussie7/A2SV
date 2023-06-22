class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(idx, transaction):
            if idx == len(prices):
                return 0
            # either we sell/buy at this index or we don't. Change the transaction state accordingly
            # transaction '1' signifies the transaction is sell there fore we add the price at this index
            if transaction == 1:
                return max(dp(idx + 1, 0) + prices[idx], dp(idx + 1, 1))
            else:
            # transaction '0' means buy so we deduct the price at this index. However, there is also a fee to be paid therefore we deduct that too
                return max(dp(idx + 1, 1) - prices[idx] - fee, dp(idx + 1, 0))

        return dp(0, 0)
