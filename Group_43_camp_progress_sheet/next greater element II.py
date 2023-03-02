class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        greaterList = [-1] * len(nums)
        for _ in range(2):
            for i in range(len(nums)):
                while stack and nums[i] > stack[-1][0]:
                    greaterList[stack.pop()[1]] = nums[i]
                
                stack.append([nums[i], i])
        
        return greaterList
