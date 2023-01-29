# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head = ListNode(-101, head)
        left = right = head
        
        while right and right.next:
            if right.next.val < x and right.val >= x:
                cutout, right.next = right.next, right.next.next

                left.next, cutout.next = cutout, left.next
                left = left.next
            else:
                right = right.next
            
            if left.next.val < x:
                left = left.next
        
        return head.next
