class Solution:
    def conquer(self, nums1, nums2):
        nums = []
        for num in nums1:
            half = bisect.bisect_left(nums2, num/2)
            if half:
                self.reversePairs += half
        
        n1 = n2 = 0
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] <= nums2[n2]:
                nums.append(nums1[n1])
                n1 += 1
            else:
                nums.append(nums2[n2])
                n2 += 1
        
        nums.extend(nums1[n1:])
        nums.extend(nums2[n2:])
        return nums

    def divide(self, nums):
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        return self.conquer(self.divide(nums[:mid]), self.divide(nums[mid:]))
    
    def reversePairs(self, nums: List[int]) -> int:
        self.reversePairs = 0
        self.divide(nums)
        return self.reversePairs
