class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # returns the bit representation of the word. (i.e.) turn on the bit in the corresponding place of the character. (e.g. for 'a' turn on bit 1, for 'j' turn on bit 10)
        def bitter(word):
            bit = 0
            offset = ord('a') - 1
            for char in list(set(word)):
                bit ^= (1 << (ord(char)-offset))
            
            return bit

        # get the bit representation of the words in 'words'
        bit_rep = {}
        for word in words:
            bit_rep[word] = bitter(word)
        
        # O(n^2) iteration to find words with different set of characters
        max_product = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # if the two words don't have a character in common compare and edit the max_prodcut so far
                if not bit_rep[words[i]] & bit_rep[words[j]]:
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product
