class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        arr_total = sum(nums)
        if arr_total % 2 == 1:
            return False

        max_val = max(nums) * n + 1
        dp = [False] * max_val
        dp[0] = True
        for i in range(1, n + 1):
            new_dp = [False] * max_val
            for j in range(max_val):
                if dp[j] == True:
                    new_dp[j] = True
                    new_dp[j + nums[i - 1]] = True
                
                if j == arr_total // 2 and new_dp[j] == True:
                    return True
            dp = new_dp

        return False



    # top-down approach
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(index, curr_sum):
            if index == len(nums) or curr_sum > arr_total // 2:
                return False

            if curr_sum == arr_total // 2:
                return True
            return dp(index + 1, curr_sum) or dp(index + 1, curr_sum + nums[index])
        
        n = len(nums)
        arr_total = sum(nums)
        return arr_total % 2 == 0 and dp(0, 0)
