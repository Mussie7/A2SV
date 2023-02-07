# O(n) time and O(1) space complexity

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        cur = head

        # get the number of nodes
        while cur:
            length += 1
            cur = cur.next
        
        # create a dummy node as head
        dummy = ListNode(-1, head)
        head = dummy

        cur = head.next
        prev = head
        
        # iterate through as many reversable batch as possible by using the length
        for i in range(length//k):
            count = 0
            patch = prev
            
            # reverse one reversable k-length batch at a time
            while count < k:
                cur.next, cur, prev = prev, cur.next, cur
                count += 1
            
            # finally patch the reverse and repeat
            patch.next.next = cur
            patch.next, prev = prev, patch.next
        
        return head.next
