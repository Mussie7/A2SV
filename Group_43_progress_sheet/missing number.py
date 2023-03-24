class Solution:
    # cycle sort
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(inf)
        for i in range(len(nums)):
            if nums[i] == inf:
                continue
            while nums[i] != i and nums[i] != inf:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        
        for i in range(len(nums)):
            if nums[i] == inf:
                return i
