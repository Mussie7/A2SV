class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return
            
        counter1 = Counter(s1)
        counter2 = Counter()
        left = 0

        for right in range(len(s2)):
            if s2[right] not in counter1:
                left = right + 1
                counter2 = Counter()
            else:
                counter2[s2[right]] += 1
                if right - left + 1 == len(s1):
                    if counter1 == counter2:
                        return True
                    else:
                        counter2[s2[left]] -= 1
                        left += 1
