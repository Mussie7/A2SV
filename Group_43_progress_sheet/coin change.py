# top-down dp approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(curr):
            if curr > amount:
                return inf
            elif curr == amount:
                return 0

            min_num = inf
            for coin in coins:
                min_num = min(min_num, dp(curr + coin))
            
            return min_num + 1
        
        ans = dp(0)
        if ans == inf:
            return -1
        return ans
      
      
# bottom-up dp approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break

                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != inf else -1
