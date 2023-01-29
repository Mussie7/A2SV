# O((n+m)*max(n,m)) time and O(n+m), where n and m are the lengths of the given words
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        merge = []
        
        while p1 < len(word1) or p2 < len(word2):
            if p1 >= len(word1):
                merge.append(word2[p2:])
                break
            
            if p2 >= len(word2):
                merge.append(word1[p1:])
                break
            
            if word1[p1] > word2[p2] or (word1[p1] == word2[p2] and word1[p1+1:] > word2[p2+1:]):
                merge.append(word1[p1])
                p1 += 1
            else:
                merge.append(word2[p2])
                p2 += 1
        
        return ''.join(merge)
