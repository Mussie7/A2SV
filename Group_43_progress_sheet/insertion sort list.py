# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5555)
        while head:
            cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next = ListNode(head.val, cur.next)
            head = head.next
        
        return dummy.next
