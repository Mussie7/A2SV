class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        preSum = [0]
        for i in range(n):
            preSum.append(candiesCount[i] + preSum[-1])
        
        print(n, preSum)
        answer = []
        for i in range(len(queries)):
            idx, days, cap = queries[i]
            answer.append(preSum[idx] // cap <= days and preSum[idx + 1] > days)
        
        return answer