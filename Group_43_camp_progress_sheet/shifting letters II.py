class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefixSum = [0] * (n+1)
        for start, end, dxn in shifts:
            if not dxn:
                add = -1
            else:
                add = 1
            prefixSum[start] += add
            prefixSum[end+1] -= add
            
        prefixSum = self.runningSum(prefixSum)
        shifted = []
        offset = ord('a')
        for i in range(n):
            current = (ord(s[i]) - offset + prefixSum[i]) % 26
            shifted.append(chr(offset+current))

        return ''.join(shifted)
