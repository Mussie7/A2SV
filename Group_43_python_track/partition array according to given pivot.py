class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        pivoted = [pivot] * n
        left, right = 0, n-1
        
        for i in range(n):
            if nums[i] < pivot:
                pivoted[left] = nums[i]
                left += 1
            
            if nums[-i-1] > pivot:
                pivoted[right] = nums[-i-1]
                right -= 1
        
        return pivoted
