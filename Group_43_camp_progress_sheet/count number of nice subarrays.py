class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odd_count = 0
        preceeding_evens = 0
        subarrays = 0
        
        for right in range(len(nums)):
            if nums[right] % 2:
                odd_count += 1
            
            if odd_count > k:
                odd_count -= 1
                left += 1
                preceeding_evens = 0

            while left < right and nums[left] % 2 == 0:
                preceeding_evens += 1
                left += 1
            
            if odd_count == k:
                subarrays += 1 + preceeding_evens

        return subarrays
