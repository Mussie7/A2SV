class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.score = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = TrieNode()
        self.offset = ord('a')

        # construct the trie and for every prefix you increment the score by one
        for word in words:
            curr = self.root
            for char in word:
                if curr.children[ord(char) - self.offset] is None:
                    curr.children[ord(char) - self.offset] = TrieNode()
                
                curr = curr.children[ord(char) - self.offset]
                curr.score += 1
        
        # for every word you sum the score of every prefix
        answer = []
        for word in words:
            score = 0
            curr = self.root
            for char in word:
                curr = curr.children[ord(char) - self.offset]
                score += curr.score
            
            answer.append(score)
        
        return answer
