class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(curr_sum):
            count = 0
            for num in nums:
                if curr_sum + num == target:
                    count += 1
                elif curr_sum + num < target:
                    count += dp(curr_sum + num)
                else:
                    break

            return count


        nums.sort()
        return dp(0)
