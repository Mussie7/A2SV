# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        answer = []
        
        index = 0
        cur = head
        while cur:
            while stack and stack[-1][1].val < cur.val:
                answer[stack[-1][0]] = cur.val
                stack.pop()
            
            stack.append([index, cur])
            answer.append(0)
            index += 1
            cur = cur.next
        
        return answer
