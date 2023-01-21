class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors_count = [0, 0, 0]
        for color in nums:
            colors_count[color] += 1
        
        i = 0
        for i in range(colors_count[0]):
            nums[i] = 0
        for i in range(colors_count[0], sum(colors_count[:2])):
            nums[i] = 1
        for i in range(sum(colors_count[:2]), sum(colors_count)):
            nums[i] = 2
