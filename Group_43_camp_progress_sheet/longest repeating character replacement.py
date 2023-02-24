class Solution:
    def checkValidity(self, counter):
        maxVal = 0
        valSum = 0
        for val in counter.values():
            maxVal = max(val, maxVal)
            valSum += val
        
        return valSum - maxVal

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        counter = Counter()
        for right in range(len(s)):
            counter[s[right]] += 1
            while self.checkValidity(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            maxLen = max(maxLen, right-left+1)
        
        return maxLen
