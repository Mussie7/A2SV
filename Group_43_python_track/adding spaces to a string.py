class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        after_spaces = [s[:spaces[0]]]
        
        for i in range(1, len(spaces)):
            after_spaces.append(s[spaces[i-1]:spaces[i]])
        
        after_spaces.append(s[spaces[-1]:])

        return " ".join(after_spaces)
