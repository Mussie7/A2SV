class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        preSumDict = Counter([0])
        preSum = 0
        subarrayCount = 0
        for num in nums:
            preSum += num
            subarrayCount += preSumDict[preSum - goal]
            preSumDict[preSum] += 1
        
        return subarrayCount
