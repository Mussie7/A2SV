# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        head = dummy

        cur = head.next
        remover = head
        counter = 1
        while cur:
            cur = cur.next
            if counter > n:
                remover = remover.next
            counter += 1
        
        remover.next = remover.next.next
        return head.next
