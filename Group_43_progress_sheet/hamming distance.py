class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bitmask = 1
        count = 0
        while bitmask <= x or bitmask <= y:
            x_bit = False if bitmask > x else bitmask | x == x
            y_bit = False if bitmask > y else bitmask | y == y
            count += (x_bit != y_bit)
            bitmask <<= 1
        
        return count
