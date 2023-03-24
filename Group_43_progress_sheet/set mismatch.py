# cycle sort solution
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i, num in enumerate(nums):
            if num != i + 1:
                return [num, i+1]

# math solution
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        supposed_to_be = (len(nums) * (len(nums) + 1)) // 2
        what_is = sum(nums)
        what_is_set = sum(set(nums))
        return [what_is - what_is_set, supposed_to_be - what_is_set]
