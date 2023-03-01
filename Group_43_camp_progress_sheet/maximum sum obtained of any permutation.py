class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for start, end in requests:
            preSum[start] += 1
            preSum[end+1] -= 1
        
        preSum.pop()
        for i in range(1, n):
            preSum[i] += preSum[i-1]
        
        preSum.sort()
        nums.sort()
        totalSum = 0
        for i in range(n):
            totalSum += nums[i] * preSum[i]
        
        return totalSum % 1000000007
