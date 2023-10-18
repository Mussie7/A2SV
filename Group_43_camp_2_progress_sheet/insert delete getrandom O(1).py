class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.randomList = []
        self.size = 0

    def insert(self, val: int) -> bool:
        # insert is a simple function
        # hold the index of the element as you insert it into the random list
        if val not in self.index_map:
            self.randomList.append(val)
            self.index_map[val] = self.size
            self.size += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        
        # here is where the magic happens
        # swap the element to be deleted with the element at the last index
        # don't forget to update the index map
        # after, just pop
        idx1 = self.index_map[val]
        idx2 = self.size - 1
        val2 = self.randomList[idx2]

        # swap
        self.index_map[val2] = idx1
        self.randomList[idx1] = val2

        # remove
        self.randomList.pop()
        del self.index_map[val]
        self.size -= 1

        return True

    def getRandom(self) -> int:
        # return random
        return random.choice(self.randomList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
