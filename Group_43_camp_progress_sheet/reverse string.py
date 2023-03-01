class Solution:
    def reverseString(self, s: List[str], i=0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if i == len(s)//2:
            return
        
        s[i], s[-i-1] = s[-i-1], s[i]
        self.reverseString(s, i+1)
