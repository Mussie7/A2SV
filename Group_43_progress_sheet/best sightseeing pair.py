class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # use the given formula
        # divide the formula to match the values to their index it becomes
        # (values[i] + i) + (values[j] - j)
        # if we can maximize these two expressions we would consequently have the maximum score
        # the dp part comes in when trying to find the best j for a given i. you would have to compute for all j that come after i. instead start from back and use only the maximum obtained so far
        n = len(values)
        dp = values[n-1] - (n-1)
        max_score = -math.inf
        for i in range(n-2, -1, -1):
            max_score = max(max_score, values[i] + i + dp)
            dp = max(dp, values[i] - i)
        
        return max_score
