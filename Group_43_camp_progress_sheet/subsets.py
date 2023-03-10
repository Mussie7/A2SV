class Solution:
    def makeSubsets(self, index, subset):
        if index == len(self.nums):
            self.subsets.append(subset.copy())
            return
        
        subset.append(self.nums[index])
        self.makeSubsets(index+1, subset)
        subset.pop()
        self.makeSubsets(index+1, subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.subsets = []
        self.makeSubsets(0, [])

        return self.subsets
