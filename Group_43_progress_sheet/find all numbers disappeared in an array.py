class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    break
                
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        ans = []
        for i, num in enumerate(nums):
            if num != i + 1:
                ans.append(i+1)
        return ans
