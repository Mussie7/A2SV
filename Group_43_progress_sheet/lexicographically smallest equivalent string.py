class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        # path compression
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        self.rep[rep2] = rep1
            
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        offset = ord('a')
        self.rep = {chr(offset + i): chr(offset + i) for i in range(26)}
        min_chr = {chr(offset + i): chr(offset + i) for i in range(26)}

        for i in range(len(s1)):
            char = min(min_chr[self.find(s1[i])], min_chr[self.find(s2[i])])
            self.union(s1[i], s2[i])
            min_chr[self.find(s1[i])] = char
        
        smallest_equivalent = ''
        for char in baseStr:
            smallest_equivalent += min_chr[self.find(char)]
        return smallest_equivalent
