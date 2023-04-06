class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        partition = 0
        for val in Counter(deck).values():
            partition = gcd(partition, val)
            if partition == 1:
                return False
        
        return True
      
    # one liner code
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return gcd(*Counter(deck).values()) > 1
