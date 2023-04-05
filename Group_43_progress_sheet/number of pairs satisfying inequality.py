class Solution:
    def conquer(self, left, right):
        l = 0
        for val in right:
            while l < len(left) and val + self.diff >= left[l]:
                l += 1
            self.pairs += l
        
        l = r = 0
        merged = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        
        merged.extend(left[l:])
        merged.extend(right[r:])
        return merged


    def divide(self, nums):
        if len(nums) == 1:
            return nums
        
        n = len(nums)
        return self.conquer(self.divide(nums[:n//2]), self.divide(nums[n//2:]))

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]
        
        self.diff = diff
        self.pairs = 0
        self.divide(nums1)
        return self.pairs
