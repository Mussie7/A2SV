class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = inf
        second = [inf, inf]
        for num in nums:
            if num < first:
                first = num
                if second[0] == inf or second[1] == inf:
                    second[0] = num
            
            elif second[0] != inf and num < second[1] and num > first:
                second[0] = first
                second[1] = num
            
            elif second[1] != inf and second[1] < num:
                return True
        
        return False
