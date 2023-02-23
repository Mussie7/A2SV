class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        max_sum = -inf
        cur_sum = 0
        for end in range(len(nums)):
            cur_sum += nums[end]
            if end >= k-1:
                max_sum = max(max_sum, cur_sum/k)
                cur_sum -= nums[start]
                start += 1
        
        return max_sum
