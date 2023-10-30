class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        presum = [0] * 101
        offset = 1950
        for birth, death in logs:
            presum[birth - offset] += 1
            presum[death - offset] -= 1
        
        max_pop = presum[0]
        target_year = offset
        for i in range(1, len(presum)):
            presum[i] += presum[i - 1]
            if presum[i] > max_pop:
                max_pop = presum[i]
                target_year = offset + i
        
        return target_year