class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        
        nums.sort()
        output = [0] * len(nums)
        last = 0
        
        for i in range(1, len(nums)):
            if nums[i][0] != nums[i-1][0]:
                last = i
            
            output[nums[i][1]] = last
        
        return output
