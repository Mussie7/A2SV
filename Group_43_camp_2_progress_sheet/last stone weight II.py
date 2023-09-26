class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def dp(index, curr_sum):
            if index == len(stones):
                return curr_sum

            # check which is optimal to take the positive or negative of the current stone
            pos = dp(index + 1, curr_sum + stones[index])
            neg = dp(index + 1, curr_sum - stones[index])

            # a negative sum doesn't make sense so ignore it when it arrives
            if neg < 0:
                return pos
            if pos < 0:
                return neg
            return min(neg, pos)
        
        return dp(0, 0)
