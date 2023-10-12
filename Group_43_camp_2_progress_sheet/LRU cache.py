class Node:
    def __init__(self, val, nxt=None, prev=None, key=None):
        self.val = val
        self.next = nxt
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.capacity = capacity
        self.size = 0
        self.keyMap = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.keyMap:
            # since it is used most recently
            self.put(key, self.keyMap[key].val)
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # adding a new pair when capacity is reached
        if key not in self.keyMap and self.size == self.capacity:
            del self.keyMap[self.tail.prev.key]
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.size -= 1

        # already exisiting pair
        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        # creating a new pair
        else:
            node = Node(value, key=key)
            self.keyMap[key] = node
            self.size += 1

        # inserting the node infront
        self.head.next, node.next = node, self.head.next
        node.next.prev = node
        node.prev = self.head

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
