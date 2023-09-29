class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.key_value_map = defaultdict(int)
        self.offset = ord('a')
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            if curr.children[ord(char) - self.offset] is None:
                curr.children[ord(char) - self.offset] = TrieNode()

            # make sure to check whether the key has been given before
            curr = curr.children[ord(char) - self.offset]
            curr.value += val - self.key_value_map[key]
        
        self.key_value_map[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if curr.children[ord(char) - self.offset] is None:
                return 0
            
            curr = curr.children[ord(char) - self.offset]
        return curr.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
