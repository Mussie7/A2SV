class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(index1, index2):
            if index1 == len(nums1) or index2 == len(nums2):
                return 0

            lines = 0
            if nums1[index1] == nums2[index2]:
                lines = dp(index1 + 1, index2 + 1) + 1
            
            lines = max(lines, dp(index1 + 1, index2), dp(index1, index2 + 1))

            return lines
        
        return dp(0, 0)
