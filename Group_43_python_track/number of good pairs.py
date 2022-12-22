class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        output = 0
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            
            output += counter[num] - 1
        
        return output
