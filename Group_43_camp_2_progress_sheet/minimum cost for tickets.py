class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * 367
        idx = n - 1
        for i in range(len(dp) - 2, -1, -1):
            dp[i] = dp[i + 1]
            if idx >= 0 and days[idx] == i:
                dp[i] = min(costs[0] + dp[min(366, i + 1)],
                            costs[1] + dp[min(366, i + 7)],
                            costs[2] + dp[min(366, i + 30)])
                idx -= 1
        
        return dp[0]



    # top-down approach
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(index, untilDay):
            if index == n:
                return 0
            
            if days[index] > untilDay:
                return min(dp(index + 1, days[index]) + costs[0],
                        dp(index + 1, days[index] + 6) + costs[1],
                        dp(index + 1, days[index] + 29) + costs[2])
            return dp(index + 1, untilDay)
        
        n = len(days)
        return dp(0, 0)
