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

# O(n) instead of O(26n)
class Solution:
    '''No need to decrement max frequency because I can't get a better one.
    What is asked of me is the longest substring I can find by replacing k different characters and making the substring consist of only one character.
    And I can only do that by finding the character with the most repetition that works by the previous rule.
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        maxFreq = 0
        counter = Counter()
        for right in range(len(s)):
            counter[s[right]] += 1
            maxFreq = max(maxFreq, counter[s[right]])
            while right - left + 1 - maxFreq > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            maxLen = max(maxLen, right-left+1)
        
        return maxLen
