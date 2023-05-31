class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n

        nums = [0] * (n + 1)
        nums[1] = 1
        max_num = 1
        for i in range(n + 1):
            if i % 2:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            else:
                nums[i] = nums[i // 2]
            
            if nums[i] > max_num:
                max_num = nums[i]
        
        return max_num
