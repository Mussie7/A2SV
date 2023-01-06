class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numsIndex = {}
        for i in range(len(nums)):
            numsIndex[nums[i]] = i
        
        for operation in operations:
            nums[numsIndex[operation[0]]] = operation[1]
            numsIndex[operation[1]] = numsIndex[operation[0]]
            del numsIndex[operation[0]]
        
        return nums
