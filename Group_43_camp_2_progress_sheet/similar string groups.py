class Solution:
    def find(self, word):
        if self.rep[word] == word:
            return word
        self.rep[word] = self.find(self.rep[word])
        return self.rep[word]
    
    def union(self, word1, word2):
        rep1, rep2 = self.find(word1), self.find(word2)
        if rep1 == rep2:
            return
        
        self.rep_count -= 1
        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]

    def numSimilarGroups(self, strs: List[str]) -> int:
        def areSimilar(word1, word2):
            word_len = len(word1)
            diff_count = 0
            for i in range(word_len):
                if word1[i] != word2[i]:
                    diff_count += 1
                
                if diff_count > 2:
                    return False
            return True

        strs = list(set(strs))
        n = len(strs)
        self.rep = {word: word for word in strs}
        self.rank = {word: 1 for word in strs}
        self.rep_count = n
        for i in range(n):
            for j in range(i + 1, n):
                if areSimilar(strs[i], strs[j]):
                    self.union(strs[i], strs[j])
        
        return self.rep_count
