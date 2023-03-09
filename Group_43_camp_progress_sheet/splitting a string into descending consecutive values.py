class Solution:
    def splitter(self, l, r):
        # check if the right pointer has reached the end and the string has been split
        # this is the base case which decides if we've reached a solution
        if r == len(self.s) and l != 0:
            return True
        
        # iterate over the next candidates
        for i in range(r, len(self.s)):
            # check if there is no previous or the new portion is a valid one
            if l == -1 or (int(self.s[l:r]) - int(self.s[r:i+1]) == 1):
                # check if a solution has beeb found
                if self.splitter(r, i+1):
                    return True
            # break if the current candidate is bigger or equal with the previous
            elif int(self.s[r:i+1]) >= int(self.s[l:r]):
                return False

    def splitString(self, s: str) -> bool:
        self.s = s
        return self.splitter(-1, 0)
