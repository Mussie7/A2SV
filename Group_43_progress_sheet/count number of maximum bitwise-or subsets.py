class Solution:
    def makeSubsets(self, curr, index):
        # if I already reach the maximum bitwise or then all iterations from now on will result in the maximum bitwise or
        if curr == self.max_or:
            self.subsets_count += 1 << (len(self.nums) - index)
            return
        # return when index out of bound
        if index == len(self.nums):
            return
        
        # place the current element and call function
        self.makeSubsets(curr | self.nums[index], index + 1)
        # call function with out placing the current element
        self.makeSubsets(curr, index + 1)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.nums = nums
        self.max_or = 0
        # the maximum bitwise or the array will have is the bitwise or between every element
        for num in nums:
            self.max_or |= num

        self.subsets_count = 0
        self.makeSubsets(0, 0)

        return self.subsets_count
