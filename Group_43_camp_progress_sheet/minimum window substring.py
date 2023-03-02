class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        sCounter = Counter()
        excess = Counter()

        left = 0
        minWindow = ''
        for right in range(len(s)):
            while left < right and s[left] not in tCounter:
                left += 1
                
            if s[right] in tCounter:
                if sCounter[s[right]] == tCounter[s[right]]:
                    excess[s[right]] += 1
                else:
                    sCounter[s[right]] += 1
            
            while sCounter == tCounter:
                if (right-left+1 < len(minWindow)) or not minWindow:
                    minWindow = s[left:right+1]
                
                if s[left] in excess:
                    excess[s[left]] -= 1
                    if excess[s[left]] == 0:
                        del excess[s[left]]
                elif s[left] in sCounter:
                    sCounter[s[left]] -= 1
                    if sCounter[s[left]] == 0:
                        del sCounter[s[left]]
                
                left += 1
        
        return minWindow
