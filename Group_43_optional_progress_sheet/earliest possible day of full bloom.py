# O(nlogn) time and O(n) space complexity

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        grow_plant = []

        # tie the planting and growing time of a seed together
        for i in range(n):
            grow_plant.append([growTime[i], plantTime[i]])
        
        # sort the newarray by the growing time and by the planting time from highest to lowest
        grow_plant.sort(reverse=True)
        # it will take atleast the planting and growing time of the seed with the highest growing time to get the earliest bloom time
        earliest_bloom = sum(grow_plant[0])

        # instantiate the growing time of the first element as leftover time
        leftover = grow_plant[0][0]

        for i in range(1, n):
            # deduct the planting time of the current seed from the leftover time
            leftover -= grow_plant[i][1]
            
            # if the leftover doesn't encompass the growth time of the current seed update the earliest time
            if leftover < grow_plant[i][0]:
                # add the time it will take to wait for the current seed to grow after deducting the leftover time
                earliest_bloom += grow_plant[i][0] - leftover
                # now the leftover is the time it takes for the current seed to grow
                leftover = grow_plant[i][0]
            
        return earliest_bloom
