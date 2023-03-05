class Solution:
    def calcFreq(self, s):
        counter = Counter(s)
        return counter[min(counter.keys())]
    
    def bs(self, freq):
        left, right = -1, len(self.freqs)
        while left + 1 < right:
            mid = left + (right-left) // 2
            if self.freqs[mid] <= freq:
                left = mid
            else:
                right = mid
        
        return len(self.freqs) - right

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        self.freqs = []
        for word in words:
            self.freqs.append(self.calcFreq(word))
        self.freqs.sort()

        frequentWords = []
        for query in queries:
            freq = self.calcFreq(query)
            frequentWords.append(self.bs(freq))
        
        return frequentWords
