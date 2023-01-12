class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for column in zip(*strs):
            if column != tuple(sorted(column)):
                count += 1

        return count

# better code in terms of space complexity
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i][j] < strs[i-1][j]:
                    count += 1
                    break
        
        return count
