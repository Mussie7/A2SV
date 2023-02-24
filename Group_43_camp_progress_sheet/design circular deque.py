class Node:
    def __init__(self, val:int, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.tail = self.head
        self.size = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.length == self.size:
            return False

        node = Node(value, self.head.next, self.head)
        self.head.next = node

        if self.tail == self.head:
            self.tail = node
        else:
            node.next.prev = node
        
        self.length += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.length == self.size:
            return False

        node = Node(value, None, self.tail)
        self.tail.next = node
        self.tail = node

        self.length += 1
        
        return True

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        
        if self.tail == self.head.next:
            self.tail = self.head
        else:
            self.head.next.next.prev = self.head
        
        self.head.next = self.head.next.next


        self.length -= 1

        return True

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False

        self.tail = self.tail.prev
        self.tail.next = None

        self.length -= 1

        return True

    def getFront(self) -> int:
        if self.length == 0:
            return -1

        return self.head.next.val

    def getRear(self) -> int:
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
