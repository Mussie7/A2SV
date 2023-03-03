class Solution:
    def checkCounters(self, c, r):
        if len(c) < len(r):
            return False

        for char in c:
            if c[char] < r[char]:
                return False
        
        return True

    def balancedString(self, s: str) -> int:
        reference = Counter(s)
        for char in list(reference.keys()):
            reference[char] -= len(s) // 4
            if reference[char] <= 0:
                del reference[char]

        if len(reference) == 0:
            return 0
        
        left = 0
        minLen = inf
        counter = Counter()
        for right in range(len(s)):
            if s[right] in reference:
                counter[s[right]] += 1
            
            while self.checkCounters(counter, reference):
                minLen = min(minLen, right - left + 1)
                if s[left] in counter:
                    counter[s[left]] -= 1
                
                left += 1
        
        return minLen
