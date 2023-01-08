class Solution:
    # my first algorithm with a worst case runtime of O(N^2)
    
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        # hold the index of every ball
        location = [i for i in range(n) if boxes[i] == '1']
        answer = []

        for box in range(n):
            ans = 0
            # take the distance of every ball to each box and add
            for ball in location:
                ans += abs(box - ball)
            
            answer.append(ans)
        
        return answer
      
    
    # A better algorithm with a runtime of O(N) 
    def operations_counter(self, start, end, jump, boxes, answer):
        count = operation = 0
        for i in range(start, end, jump):
            # counts the number of balls behind or after the box
            if boxes[i-jump] == '1':
                count += 1
            
            # count how many moves it will take to bring the balls behind or after the box
            operation += count
            answer[i] += operation

    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        # left_counter
        self.operations_counter(1, n, 1, boxes, answer)
        # right_counter
        self.operations_counter(n-2, -1, -1, boxes, answer)

        return answer
