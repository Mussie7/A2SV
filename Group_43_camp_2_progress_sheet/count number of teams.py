class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        incCount = [0] * n
        decCount = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    incCount[i] += 1
                if rating[j] < rating[i]:
                    decCount[i] += 1
        
        triplets = 0
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    triplets += incCount[j]
                if rating[j] < rating[i]:
                    triplets += decCount[j]
        
        return triplets
