class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        incStack = []
        subarrayMinSums = 0
        stackSum = 0
        for i in range(len(arr)):
            count = 1
            while incStack and arr[i] <= incStack[-1][0]:
                last = incStack.pop()
                stackSum -= last[0] * last[1]
                count += last[1]
            
            incStack.append([arr[i], count])
            stackSum += arr[i] * count
            subarrayMinSums += stackSum
        
        return (subarrayMinSums % 1000000007)
