class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = [0] * k
        remainder[0] += 1
        subarray = 0
        preSum = 0

        for num in nums:
            preSum += num
            subarray += remainder[preSum%k]
            remainder[preSum%k] += 1
        
        return subarray
