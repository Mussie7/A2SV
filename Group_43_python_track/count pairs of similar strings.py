class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter = {}
        output = 0
        for word in words:
            temp = list(set(word))
            temp.sort()
            temp = tuple(temp)
            if temp in counter:
                counter[temp] += 1
            else:
                counter[temp] = 1
            
            output += counter[temp] - 1
        
        print(counter)
        return output
