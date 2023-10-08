class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        final = [gas[i] - cost[i] for i in range(n)]
        final.extend(final)

        left, right = 0, 0
        gas_sum = 0
        while right < 2 * n:
            gas_sum += final[right]
            while gas_sum < 0:
                gas_sum -= final[left]
                left += 1
            
            if right - left + 1 == n:
                return left
            
            right += 1
        return -1
