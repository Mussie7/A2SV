# Definition for singly-linked list.
# class ListNode:
#     def __lt__(self, other):
#         return self.val < other.val

#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# heap implementation
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for cur_list in lists:
            cur = cur_list
            while cur:
                heapq.heappush(heap, [cur.val, ListNode(cur.val)])
                cur = cur.next
        
        new_list = ListNode()
        cur = new_list
        while heap:
            cur.next = heapq.heappop(heap)[1]
            cur = cur.next
        
        return new_list.next
      
      
      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __lt__(self, other):
#         return self.val < other.val

# merge sort implementation
class Solution:
    def merge2Lists(self, cur1, cur2):
        newList = cur = ListNode()
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            
            cur = cur.next
        
        cur.next = cur1 or cur2
        return newList.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not n:
            return
        elif n == 1:
            return lists[0]

        left = self.mergeKLists(lists[:n//2])
        right = self.mergeKLists(lists[n//2:])
        return self.merge2Lists(left, right)
      
      
      
      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# merge-sort-like algo implementation
class Solution:
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

    # great solution btw
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            merged = []
            remainder = len(lists) % 2
            
            for i in range(0, len(lists)-remainder, 2):
                merged.append(self.merge2Lists(lists[i], lists[i+1]))
            
            if remainder:
                merged.append(lists[-1])
            
            lists = merged
        
        return lists[0] if lists else None
