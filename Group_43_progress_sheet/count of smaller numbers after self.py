class Solution:
    def conquer(self, left, right):
        i = 0
        for index in left:
            while i < len(right) and self.nums[index] > self.nums[right[i]]:
                i += 1
            self.counts[index] += i
        
        merge = []
        l = r = 0
        while l < len(left) and r < len(right):
            if self.nums[left[l]] < self.nums[right[r]]:
                merge.append(left[l])
                l += 1
            else:
                merge.append(right[r])
                r += 1
        
        merge.extend(left[l:])
        merge.extend(right[r:])
        return merge

    def divide(self, nums):
        if len(nums) == 1:
            return nums
        
        n = len(nums)
        return self.conquer(self.divide(nums[:n//2]), self.divide(nums[n//2:]))

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.counts = [0] * n
        self.nums = nums
        index_nums = [i for i in range(n)]

        self.divide(index_nums)
        return self.counts
