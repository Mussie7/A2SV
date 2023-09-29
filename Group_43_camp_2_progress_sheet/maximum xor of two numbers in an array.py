class Solution:
    def insert(self, word: str) -> None:
        curr = self.root
        for bit in map(int, word):
            if curr[bit] is None:
                curr[bit] = [None, None]
            
            curr = curr[bit]
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        self.root = [None, None]

        for i, num in enumerate(nums):
            binary = bin(num)[2:]
            binary = '0' * (32 - len(binary)) + binary
            self.insert(binary)
            nums[i] = binary
        
        maximum_xor = 0
        for num in nums:
            curr = self.root
            xor = []
            for bit in map(int, num):
                if curr[int(not bit)]:
                    xor.append('1')
                    curr = curr[int(not bit)]
                else:
                    xor.append('0')
                    curr = curr[bit]
            maximum_xor = max(maximum_xor, int(''.join(xor), 2))
        
        return maximum_xor
