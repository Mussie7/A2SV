class Solution:
    def minSteps(self, n: int) -> int:
        # we are certain there is always going to be some number of operations that can result in n number of characters for n > 0.
        @cache
        def dp(curr, prev_copy):
            # if your current number of characters is greater than n it is not an eligible answer therefore you have to make sure it doesn't pass the min() function
            if curr > n:
                return inf
            # valid base case
            if curr == n:
                return 0
            # for the first instance it is always going to be 2 operations, first copy then paste 
            if prev_copy == 0:
                return dp(curr + curr, curr) + 2

            # choose the optimal between pasting the first which is one operation or copy-pasting the current which is 2 operations
            return min(dp(curr + prev_copy, prev_copy) + 1, dp(curr + curr, curr) + 2)
        
        return dp(1, 0)
