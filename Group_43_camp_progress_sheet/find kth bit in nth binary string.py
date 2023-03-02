class Solution:
    def __init__(self):
        self.converter = {'1': '0', '0': '1'}
    
    def reverseInvert(self, binary: str) -> str:
        binary = list(binary)
        left, right = 0, len(binary) - 1
        while left <= right:
            binary[left] = self.converter[binary[left]]
            if left < right:
                binary[right] = self.converter[binary[right]]
                binary[left], binary[right] = binary[right], binary[left]
            
            left += 1
            right -= 1
        
        return ''.join(binary)
        
    def stringMaker(self, n):
        if n == 1:
            return '0'
        
        newStr = [self.stringMaker(n-1)]
        newStr.append('1')
        newStr.append(self.reverseInvert(newStr[0]))
        
        return ''.join(newStr)
      
    def findKthBit(self, n: int, k: int) -> str:
        return self.stringMaker(n)[k-1]
