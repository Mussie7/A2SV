class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)-1):
            if nums[i] == 0:
                continue
            
            if nums[i] == nums[i + 1]:
                output.append(nums[i] * 2)
                nums[i+1] = 0
            else:
                output.append(nums[i])
        
        if nums[-1] != 0:
            output.append(nums[-1])
        
        return output + [0] * (len(nums) - len(output))
