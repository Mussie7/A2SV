class Solution:
    def backtrack(self, index, tracker, n):
        if tracker == (2 ** n) - 1:
            self.count += 1
            return
        
        for i in range(n):
            mask = 1 << i
            if not tracker & mask and (not (i + 1) % index or not index % (i + 1)):
                tracker |= mask
                self.backtrack(index + 1, tracker, n)
                tracker &= ~mask

    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.backtrack(1, 0, n)
        return self.count
