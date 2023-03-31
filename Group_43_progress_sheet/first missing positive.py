class Solution:
    # cyclic sort
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != i + 1:
                if nums[nums[i]-1] == nums[i]:
                    break
                    
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i] - 1]
                if nums[i] <= 0 or nums[i] > len(nums):
                    break
        
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return len(nums) + 1
    
    # counting sort
    def firstMissingPositive(self, nums: List[int]) -> int:
        counting = [0] * 100000
        for num in nums:
            if 0 < num < 100001:
                counting[num-1] = 1
        
        for index, num in enumerate(counting):
            if num == 0:
                return index + 1
        
        return 100001
