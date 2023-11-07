class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        dec_stack = []
        right_see = [0 for i in range(n)]
        for i in range(n):
            while dec_stack and heights[i] >= heights[dec_stack[-1]]:
                right_see[dec_stack[-1]] += 1
                dec_stack.pop()
            
            if dec_stack:
                right_see[dec_stack[-1]] += 1
            dec_stack.append(i)
        
        return right_see