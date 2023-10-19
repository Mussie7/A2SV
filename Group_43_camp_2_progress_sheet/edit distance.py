class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(index1, index2):
            if len(word1) == index1:
                return len(word2) - index2
            if len(word2) == index2:
                return len(word1) - index1
            
            if word1[index1] == word2[index2]:
                return dp(index1 + 1 , index2 + 1)
                
            insert = 1 + dp(index1, index2 + 1)
            delete = 1 + dp(index1 + 1 , index2)
            replace = 1 + dp(index1 + 1, index2 + 1)
            return min(insert, delete, replace)
        
        return dp(0, 0)
