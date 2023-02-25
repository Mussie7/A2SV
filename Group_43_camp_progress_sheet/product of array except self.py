class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front_preSum = [nums[0]]
        rear_preSum = [nums[-1]]
        for i in range(1, len(nums)):
            front_preSum.append(nums[i] * front_preSum[i-1])
            rear_preSum.append(nums[len(nums) - i-1] * rear_preSum[-1])
        
        rear_preSum = rear_preSum[::-1]
        otherProduct = [1] * len(nums)
        otherProduct[0] = rear_preSum[1]
        otherProduct[-1] = front_preSum[-2]
        
        for i in range(1, len(nums)-1):
            otherProduct[i] = front_preSum[i-1] * rear_preSum[i+1]
        
        return otherProduct
