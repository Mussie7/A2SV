class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        1. instantiate a stack, a score variable
        2. iterate over s
            2.1. add the opening brackets to the stack with a score of 0
            2.2. when I reach closing brackets I pop from the stack
                2.2.1. if the score of my previous bracket is zero my current score becomes 1
                  if the stack is empty add current score to the main score variable if it is not empty I increment the score of the last bracket in the stack by the current score
                2.2.2. if the score of my previous bracket is not zero I multiply its score by 2. If the stack is empty add the  current score to the main score variable if it is not empty I increment the score of the last bracket in the stack by the current score
        3. return the score variable
        '''
        stack = []
        score = 0
        for char in s:
            if char == '(':
                stack.append(0)
                continue
            
            cur_score = stack.pop()
            cur_score = max(1, cur_score*2)
            if not stack:
                score += cur_score
            else:
                stack[-1] += cur_score
        
        return score

