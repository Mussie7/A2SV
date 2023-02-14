# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        slow, fast = head, head.next
        # check if fast is also none for the edge case - the given list has length of 1
        while fast and fast.next and fast.next.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        stack.append(slow.val)
        # the previous edge case also applies here
        # if the length of the list is odd dismiss the middle node by jumping over
        if fast and fast.next:
            slow = slow.next.next
        else:
            slow = slow.next
        
        while slow and slow.val == stack[-1]:
            stack.pop()
            slow = slow.next
        
        return not slow
