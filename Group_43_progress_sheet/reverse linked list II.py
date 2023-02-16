# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-555, head)
        head = dummy
        
        count, cur = 0, head
        while count < left-1:
            count += 1
            cur = cur.next

        patch1 = cur

        prev = cur
        cur = cur.next
        while count < right:
            count += 1
            cur.next, cur, prev = prev, cur.next, cur
        
        patch1.next.next = cur
        patch1.next = prev
        
        return head.next
