class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @cache
        def dp(index, sign):
            max_subsequence = 1
            for i in range(index + 1, n):
                if (nums[i] - nums[index]) != 0 and (nums[i] - nums[index]) // abs(nums[i] - nums[index]) == -sign:
                    max_subsequence = max(max_subsequence, dp(i, -sign) + 1)
                
            return max_subsequence

        n = len(nums)
        return max(dp(0, 1), dp(0, -1))



# O(n) solution
# the number of turning points is directly related to the number of elements in the wiggle subsequence
# turning point - change in sign of difference between adjacent elements
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = 1
        sign = 0
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) != 0 and (nums[i] - nums[i-1]) // abs(nums[i] - nums[i-1]) != sign:
                length += 1
                sign = (nums[i] - nums[i-1]) // abs(nums[i] - nums[i-1])
        
        return length
