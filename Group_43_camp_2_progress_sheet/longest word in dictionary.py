class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        def retrieve(node, curr):
            nonlocal longest, offset
            # base case - if the current path isn't a word it defies the requirements of the question
            if not node.is_end_of_word:
                return

            # update the longest word
            if len(curr) > len(longest):
                longest = curr

            for i, child in enumerate(node.children):
                if child:
                    retrieve(child, curr + chr(i + offset))


        root = TrieNode()
        root.is_end_of_word = True
        offset = ord('a')
        # perform a normal insertion operation for every word in words into the root trie
        for word in words:
            curr = root
            for char in word:
                if curr.children[ord(char) - offset] is None:
                    curr.children[ord(char) - offset] = TrieNode()
                
                curr = curr.children[ord(char) - offset]
            
            curr.is_end_of_word = True
        
        longest = ''
        # retrieve the longest word
        retrieve(root, '')
        return longest
