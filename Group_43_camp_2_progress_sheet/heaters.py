class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        for house in houses:
            # find the nearest heater for every house
            idx = bisect.bisect_left(heaters, house)
            curr_radius = inf
            # compute the radius of the nearest heater for every house
            if idx < len(heaters):
                curr_radius = min(curr_radius, abs(heaters[idx] - house))
            if idx > 0:
                curr_radius = min(curr_radius, abs(heaters[idx - 1] - house))

            # compare the maximum distance of the nearest heater for all the houses
            radius = max(radius, curr_radius)
        
        return radius
