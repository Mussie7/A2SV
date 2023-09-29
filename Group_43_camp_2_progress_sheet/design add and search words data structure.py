class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.offset = ord('a')

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.children[ord(char) - self.offset] is None:
                curr.children[ord(char) - self.offset] = TrieNode()
            
            curr = curr.children[ord(char) - self.offset]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def searcher(index, node):
            if index == len(word):
                return node.is_end_of_word
            
            place = ord(word[index]) - self.offset
            # if the current character is not a dot you return true if the current character exists as a child and it leads to the word
            if word[index] != '.':
                return node.children[place] and searcher(index + 1, node.children[place])
            
            for child in node.children:
                if child and searcher(index + 1, child):
                    return True                
            
            return False

        return searcher(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
