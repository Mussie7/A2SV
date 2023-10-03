class TrieNode():
    def __init__(self):
        self.children = [None] * 27
        self.is_end_of_word = False
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.offset = ord('a')
        for index, word in enumerate(words):
            self.insert(word, index)

    def insert(self, word: str, index: int) -> None:
        n = len(word)
        word += '{' + word
        for i in range(n):
            curr = self.root
            for char in word[i:]:
                if curr.children[ord(char) - self.offset] is None:
                    curr.children[ord(char) - self.offset] = TrieNode()
                
                curr = curr.children[ord(char) - self.offset]
                curr.index = index

    def f(self, pref: str, suff: str) -> int:
        word = suff + '{' + pref
        curr = self.root
        for char in word:
            if curr.children[ord(char) - self.offset] is None:
                return -1
            
            curr = curr.children[ord(char) - self.offset]
        
        return curr.index


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

# P.S. I had to look at the hint to solve this question
