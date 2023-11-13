class Solution:
    def backtrack(self, open, close, curr_par):
        if open == close == 0:
            self.par.append(''.join(curr_par))
            return
        
        if open > 0:
            curr_par.append('(')
            self.backtrack(open - 1, close + 1, curr_par)
            curr_par.pop()
        
        if close > 0:
            curr_par.append(')')
            self.backtrack(open, close - 1, curr_par)
            curr_par.pop()
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.par = []
        self.backtrack(n, 0, [])
        return self.par
