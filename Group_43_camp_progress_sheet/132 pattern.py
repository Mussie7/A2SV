class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        decStack = []
        two = -inf
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < two:
                return True
            
            while decStack and nums[i] > decStack[-1]:
                two = decStack.pop()
            decStack.append(nums[i])
        
        return False
