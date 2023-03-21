class Solution:
    # backtracking solution
    def makeSequences(self, index, seq):
        if len(seq) > 1:
            self.sequences.add(tuple(seq))
        
        if index == len(self.nums):
            return
        
        if not seq or self.nums[index] >= seq[-1]:
            seq.append(self.nums[index])
            self.makeSequences(index + 1, seq)
            seq.pop()
        self.makeSequences(index + 1, seq)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.sequences = set()
        self.makeSequences(0, [])

        return self.sequences
