# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2, cur):
        if not list1:
            cur.next = list2
            return
        elif not list2:
            cur.next = list1
            return
        elif list1.val < list2.val:
            cur.next = list1
            self.merge(list1.next, list2, cur.next)
        else:
            cur.next = list2
            self.merge(list1, list2.next, cur.next)
        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.head = ListNode(-111)
        self.merge(list1, list2, self.head)
        return self.head.next
