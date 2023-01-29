# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNode(self, node):
        removed = node.next
        node.next = node.next.next
        
        return removed
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        
        if head.val < x:
            left = head
            while left.next:
                if left.next.val >= x:
                    break
                
                left = left.next
        else:
            left = ListNode(-101, head)
        
        right = left
        while right and right.next:
            if right.next.val < x:
                cutout = self.removeNode(right)

                if left.val == -101:
                    left.val = cutout.val
                    head = left
                else:
                    left.next, cutout.next = cutout, left.next
                    left = left.next
            else:
                right = right.next
        
        return head
