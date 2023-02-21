# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        dummy = ListNode(-101, head)
        head = dummy
        prev = head.next
        cur = head.next.next

        while cur:
            if cur.val != prev.val and prev != head.next:
                head.next = cur
            elif cur.val != prev.val:
                head = head.next
            
            prev = cur
            cur = cur.next
        
        if head.next != prev:
            head.next = cur

        return dummy.next
