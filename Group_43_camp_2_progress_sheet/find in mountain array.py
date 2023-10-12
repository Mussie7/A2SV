# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def bs(left, right, reverse):
            found_value = -1
            while left + 1 < right:
                mid = left + (right - left) // 2
                mid_value = mountain_arr.get(mid)
                if reverse:
                    if mid_value <= target:
                        right = mid
                        found_value = mid_value
                    else:
                        left = mid
                else:
                    if mid_value >= target:
                        right = mid
                        found_value = mid_value
                    else:
                        left = mid
            
            return [right, found_value]

        n = mountain_arr.length()
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid - 1):
                left = mid
            else:
                right = mid
        
        peak = left
        for i, (left, right) in enumerate([[-1, peak + 1], [peak - 1, n]]):
            idx, val = bs(left, right, bool(i))
            if val == target:
                return idx
        
        return -1
