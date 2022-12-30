class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        curSum = 0

        for num in nums:
            if not num % 2:
                curSum += num
        
        for query in queries:
            if not nums[query[1]] % 2:
                curSum -= nums[query[1]]
            
            nums[query[1]] += query[0]
            if not nums[query[1]] % 2:
                curSum += nums[query[1]]
            
            output.append(curSum)
        
        return output
