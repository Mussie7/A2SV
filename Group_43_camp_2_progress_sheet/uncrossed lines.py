# top_down approach
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


# bottom-up approach
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # chooseing the best with out making a line with the current indices
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
                # checking whether we can make a line with the current indices
                if nums1[i] == nums2[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j+1] + 1)
        
        return dp[0][0]
