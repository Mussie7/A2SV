# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # merges two sorted lists
    def merge2Lists(self, list1, list2):
        cur1, cur2 = list1, list2
        newList = cur = ListNode()
        
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            
            cur = cur.next
        
        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2
        
        return newList.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # check until the list has one listNode
        while len(lists) > 1:
            # merge 2 at a time and restart the cycle to reduce time complexity
            merged = []
            remainder = len(lists) % 2
            
            # if lists is odd don't merge the last one
            for i in range(0, len(lists)-remainder, 2):
                merged.append(self.merge2Lists(lists[i], lists[i+1]))
            
            # if lists is odd add the last one in the merged pile
            if remainder:
                merged.append(lists[-1])
            
            # make lists the merged list and start over until only one remains
            lists = merged
        
        # check if lists is empty when given
        return lists[0] if lists else None
