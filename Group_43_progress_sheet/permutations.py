class Solution:
    def makePermutations(self, curr):
        if len(self.curr_perm) == len(self.nums):
            self.permutations.append(self.curr_perm.copy())
            return
        
        for i in range(len(self.nums)):
            mask = 1 << i
            if not curr & mask:
                curr |= mask
                self.curr_perm.append(self.nums[i])
                self.makePermutations(curr)
                self.curr_perm.pop()
                curr &= ~mask

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.curr_perm = []
        self.nums = nums
        self.makePermutations(0)

        return self.permutations
