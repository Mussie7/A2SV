# Trie solution
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.offset = ord('a')

    def insert(self, word):
        curr = self.root
        for char in word:
            if curr.children[ord(char) - self.offset] is None:
                curr.children[ord(char) - self.offset] = TrieNode()
            
            curr = curr.children[ord(char) - self.offset]
        
        curr.count += 1

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def subseq_counter(node, limit):
            subseq_count = node.count
            for i, child in enumerate(node.children):
                if child is not None:
                    char = chr(i + self.offset)
                    index = bisect.bisect_left(index_map[char], limit)
                    if index < len(index_map[char]):
                        subseq_count += subseq_counter(child, index_map[char][index] + 1)
            
            return subseq_count

        index_map = defaultdict(list)
        for i, char in enumerate(s):
            index_map[char].append(i)
        
        for word in words:
            self.insert(word)
        
        return subseq_counter(self.root, 0)




# Binary search solution
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index_map = defaultdict(list)
        for i, char in enumerate(s):
            index_map[char].append(i)

        subseq_count = len(words)
        for word in words:
            index = 0
            for char in word:
                pos = bisect.bisect_left(index_map[char], index)
                if pos < len(index_map[char]):
                    index = index_map[char][pos] + 1
                else:
                    subseq_count -= 1
                    break
                        
        return subseq_count
