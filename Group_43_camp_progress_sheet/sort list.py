# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, node1, node2):
        list3 = ListNode()
        merged = list3
        while node1 and node2:
            if node1.val < node2.val:
                merged.next = node1
                node1 = node1.next
            else:
                merged.next = node2
                node2 = node2.next
            
            merged = merged.next
        
        merged.next = node1 or node2

        return list3.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next, slow = None, slow.next
        return self.merge(self.sortList(head), self.sortList(slow))
