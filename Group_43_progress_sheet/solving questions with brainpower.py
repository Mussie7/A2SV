class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(index):
            if index >= len(questions):
                return 0
            
            return max(questions[index][0] + dp(index + questions[index][1] + 1), dp(index + 1))
        
        return dp(0)
