# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        because k could be greater than the length of the linked list, I need the length of the linked list. Once i get the length I would modulo k by it so that I can make a valid k
        when I get the length I give the last element the reference to the head using next
        now I, again, iterate through the linked list until I am k steps away from the end and do the operations
        the operations - standing at the current element make it's reference to the next element None
            make the next element the head of the linked list
        '''
        if not head:
            return

        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head

        k %= length

        for i in range(length-k):
            cur = cur.next
        
        head = cur.next
        cur.next = None

        return head
