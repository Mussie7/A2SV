# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        cur1, cur2 = l1, l2
        while cur1 or cur2:
            if cur1:
                stack1.append(cur1)
                cur1 = cur1.next
            if cur2:
                stack2.append(cur2)
                cur2 = cur2.next
        
        new_num = ListNode()
        carry = 0
        while stack1 or stack2:
            val1 = stack1.pop().val if stack1 else 0
            val2 = stack2.pop().val if stack2 else 0            
            num = val1 + val2 + carry
            carry = int(num > 9)
            num %= 10
            new_num.val = num
            new_num = ListNode(next=new_num)
        
        if carry == 1:
            new_num.val = 1
        else:
            new_num = new_num.next
        
        return new_num
