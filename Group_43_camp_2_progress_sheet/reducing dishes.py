class Solution:
    # DP(dynamic programming) solution
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        @cache
        def dp(index, time):
            if index == n:
                return 0
            
            return max(dp(index + 1, time), dp(index + 1, time + 1) + (satisfaction[index] * time))

        
        n = len(satisfaction)
        satisfaction.sort()
        return dp(0, 1)

    # Greedy solution
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        coefficientSum = preSum = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            preSum += satisfaction[i]
            if preSum < 0:
                return coefficientSum
            coefficientSum += preSum
        
        return coefficientSum
