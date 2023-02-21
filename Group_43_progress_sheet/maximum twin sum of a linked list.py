# my solution with O(n) space and O(n) time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        slow, fast = head, head.next
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        stack.append(slow.val)
        slow = slow.next

        twin_sum = 0
        while slow:
            twin_sum = max(twin_sum, stack.pop()+slow.val)
            slow = slow.next

        return twin_sum
      
# Better solution with O(1) space and O(n) time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        prev = None
        # have a third variable to hold the previous node and reverse the first half of the list
        while fast and fast.next:
            slow.next, prev, slow = prev, slow, slow.next
            fast = fast.next.next
        
        slow.next, prev, slow = prev, slow, slow.next

        # since the list is reversed just call next until the end and use the values in the mean time
        twin_sum = 0
        while slow:
            twin_sum = max(twin_sum, prev.val+slow.val)
            slow = slow.next
            prev = prev.next
        
        return twin_sum
