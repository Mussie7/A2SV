class Solution:        
    def numTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dp(left, right):
            left_pos = 0
            for i in range(1, left + 1):
                left_pos += dp(i - 1, left - i)
            
            right_pos = 0
            for i in range(1, right + 1):
                right_pos += dp(i - 1, right - i)
            
            left_pos = max(1, left_pos)
            right_pos = max(1, right_pos)
            return left_pos * right_pos
        return dp(n, 0)
