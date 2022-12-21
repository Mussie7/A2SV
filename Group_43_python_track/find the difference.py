class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = Counter(s)
        for i in t:
            if i in sc and sc[i] > 0:
                sc[i] -= 1
            else:
                return i
