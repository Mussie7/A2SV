class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i+1
        
        cur = 0
        for r in range(len(words)):
            if dic[words[r][0]] < cur:
                return
            
            if dic[words[r][0]] == cur:
                if words[r] in words[r-1] and len(words[r]) < len(words[r-1]):
                    return
                for i in range(min(len(words[r]), len(words[r-1]))):
                    if dic[words[r][i]] < dic[words[r-1][i]]:
                        return
                    elif words[r][i] != words[r-1][i]:
                        break

            cur = dic[words[r][0]]                
        
        return True
