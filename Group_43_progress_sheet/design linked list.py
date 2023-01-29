class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        cur = self.head.next
        for i in range(index):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head.next)
        self.head.next = node
        
        if self.size == 0:
            self.tail = self.head.next

        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        cur = self.head
        for i in range(index):
            cur = cur.next
        
        node = Node(val, cur.next)
        cur.next = node
        
        if index == self.size:
            self.tail = node
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        
        cur.next = cur.next.next
        
        if index == self.size-1:
            self.tail = cur

        self.size -= 1

    def print(self):
        cur = self.head.next
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        
        print(values)
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
