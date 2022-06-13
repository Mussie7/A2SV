class Solution:        
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        optimum = [0] * (len(rides)+1)
        nex = {}
        end = sorted(rides, key=lambda rides:rides[1])
        rides.sort()
        e = 0
        for j in range(len(end)):
            while e < len(rides) and end[j][1] > rides[e][0]:
                e += 1
            nex[tuple(end[j])] = e
        
        for i in range(len(rides)-1, -1, -1):
            made = rides[i][1] - rides[i][0] + rides[i][2]
            optimum[i] = max(made + optimum[nex[tuple(rides[i])]], optimum[i+1])

        return optimum[0]
      
      # took 60 minutes
      # 3 submissions
      # dynamic programming and sorting
