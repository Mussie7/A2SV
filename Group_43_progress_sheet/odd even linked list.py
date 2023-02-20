# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        even = head.next
        cur = head
        while cur and cur.next:
            if cur.next.next:
                cur.next.next, cur.next = cur.next.next.next, cur.next.next
            else:
                # we reach the end of both the odd and even list so we cut the tie between the last odd node to the last even node
                cur.next = None
                break
                
            # since the odd node now refers to the next odd node we just move to the next one
            cur = cur.next
        
        cur.next = even
        return head
