class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(index, swapped):
            if index == n:
                return 0

            # try to figure out what the previous element is for both arrays' current element
            if index != 0 and swapped:
                prev1 = nums2[index - 1]
                prev2 = nums1[index - 1]
            elif index != 0 and not swapped:
                prev1 = nums1[index - 1]
                prev2 = nums2[index - 1]
            
            swap_count = math.inf
            # Try to swap
            # You can only do that if the array is going to be strictly increasing at the end
            if index == 0:
                swap_count = min(swap_count, dp(index + 1, True) + 1)
            elif nums2[index] > prev1 and nums1[index] > prev2:
                swap_count = min(swap_count, dp(index + 1, True) + 1)
            
            # Try to not swap
            # Same rules apply
            if index == 0:
                swap_count = min(swap_count, dp(index + 1, False))
            elif nums1[index] > prev1 and nums2[index] > prev2:
                swap_count = min(swap_count, dp(index + 1, False))
            
            return swap_count

        n = len(nums1)
        return dp(0, False)
