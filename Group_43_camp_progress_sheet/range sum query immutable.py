class NumArray:

    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.pre_nums = nums

    def sumRange(self, left: int, right: int) -> int:
        if left-1 >= 0:
            return self.pre_nums[right] - self.pre_nums[left-1]
        
        return self.pre_nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
