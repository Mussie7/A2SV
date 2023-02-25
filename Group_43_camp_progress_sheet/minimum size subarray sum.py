class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = inf
        left = 0
        windowSum = 0
        for right in range(len(nums)):
            windowSum += nums[right]
            while windowSum - nums[left] >= target:
                windowSum -= nums[left]
                left += 1
            
            if windowSum >= target:
                minLen = min(minLen, right - left + 1)
        
        return minLen if minLen != inf else 0
